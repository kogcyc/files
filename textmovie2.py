#!/usr/bin/env python3
import argparse
import io
import re
from dataclasses import dataclass
from typing import List, Tuple

import cairosvg
import imageio.v2 as imageio
import numpy as np
from PIL import Image

# --------------------------------------------------
# Defaults
# --------------------------------------------------
DEFAULT_WIDTH, DEFAULT_HEIGHT = 1920, 1080
DEFAULT_FPS = 24
DEFAULT_FONT_FAMILY = "DejaVu Sans"
DEFAULT_FONT_WEIGHT = "normal"
DEFAULT_FONT_SIZE = 48
DEFAULT_BG = "black"
DEFAULT_OUT = "textmovie.mp4"

# A built-in "teaching movie" script (uses the same DSL)
TEACH_SCRIPT = """\
list #222 #fff
This tool turns text into video, 3
All lines are shown at once, 3
One line is highlighted at a time, 3
The number sets seconds per line, 3
Colors can be names or hex (#rgb/#rrggbb), 4
Example format:, 4
list #222 white, 3
hello, 2, 3
there, 1, 3
world! 3, 5
Now write your own script file., 7
"""

# --------------------------------------------------
# DSL structures
# --------------------------------------------------
@dataclass
class Item:
    text: str
    duration: float  # seconds for which this item is active

@dataclass
class Script:
    mode: str  # currently only "list"
    inactive_color: str
    active_color: str
    items: List[Item]

# --------------------------------------------------
# Parsing
# --------------------------------------------------
HEX_COLOR = re.compile(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")

def parse_script_text(text: str) -> Script:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("//")]
    if not lines:
        raise ValueError("Script is empty.")

    header = lines[0].split()
    if len(header) < 3:
        raise ValueError('First line must look like:  list <inactive_color> <active_color>')
    if header[0].lower() != "list":
        raise ValueError('Only "list" mode is supported right now (first token must be "list").')

    inactive_color = header[1]
    active_color = header[2]

    # We intentionally accept any SVG/CSS color token (named colors, #rgb, #rrggbb, rgb(), etc).
    # Optionally warn on weird tokens; we keep it permissive.
    def maybe_warn_color(token: str) -> None:
        if token.startswith("#"):
            if not HEX_COLOR.match(token):
                # Still allow (SVG supports more forms), but flag it.
                print(f"warning: color token {token!r} doesn't look like #rgb or #rrggbb; SVG may still accept it.")
        # else: named colors / rgb() / etc — let SVG validate.

    maybe_warn_color(inactive_color)
    maybe_warn_color(active_color)

    items: List[Item] = []
    for ln in lines[1:]:
        # Expected: "some text, 2"
        if "," not in ln:
            raise ValueError(f"Expected 'text, seconds' but got: {ln!r}")
        left, right = ln.rsplit(",", 1)
        txt = left.strip()
        if not txt:
            raise ValueError(f"Empty text in line: {ln!r}")
        try:
            dur = float(right.strip())
        except ValueError:
            raise ValueError(f"Bad duration in line: {ln!r} (must be a number)") from None
        if dur <= 0:
            raise ValueError(f"Duration must be > 0 in line: {ln!r}")
        items.append(Item(text=txt, duration=dur))

    if not items:
        raise ValueError("No items found. Add lines like: hello, 2")

    return Script(mode="list", inactive_color=inactive_color, active_color=active_color, items=items)

def parse_script_file(path: str) -> Script:
    with open(path, "r", encoding="utf-8") as f:
        return parse_script_text(f.read())

# --------------------------------------------------
# Timing helpers
# --------------------------------------------------
def total_duration(script: Script) -> float:
    return sum(it.duration for it in script.items)

def active_index_at(t: float, script: Script) -> int:
    acc = 0.0
    for i, it in enumerate(script.items):
        acc += it.duration
        if t < acc:
            return i
    return len(script.items) - 1

# --------------------------------------------------
# SVG rendering
# --------------------------------------------------
def svg_escape(s: str) -> str:
    # Keep it minimal; enough to prevent accidental SVG breakage.
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
    )

def render_list_svg(
    script: Script,
    t: float,
    width: int,
    height: int,
    bg: str,
    font_family: str,
    font_weight: str,
    font_size: int,
    line_spacing: float,
    align: str,
    margin_x: int,
) -> str:
    active_i = active_index_at(t, script)

    lh = font_size * line_spacing
    block_h = (len(script.items) - 1) * lh
    start_y = height / 2 - block_h / 2

    if align == "center":
        x = "50%"
        anchor = "middle"
    elif align == "left":
        x = str(margin_x)
        anchor = "start"
    else:
        raise ValueError("align must be 'center' or 'left'")

    lines_svg = []
    for i, it in enumerate(script.items):
        y = start_y + i * lh
        color = script.active_color if i <= active_i else script.inactive_color
        # NOTE: i <= active_i means "once highlighted, stays white" (your requested behavior).
        # If you instead want only the current line white, change to: (i == active_i)

        lines_svg.append(f"""
        <text x="{x}" y="{y:.1f}"
              font-family="{font_family}"
              font-weight="{font_weight}"
              font-size="{font_size}"
              fill="{color}"
              text-anchor="{anchor}"
              dominant-baseline="middle">
          {svg_escape(it.text)}
        </text>
        """)

    return f"""\
<svg width="{width}" height="{height}"
     xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{bg}"/>
  {''.join(lines_svg)}
</svg>
"""

# --------------------------------------------------
# Frame generation & encoding
# --------------------------------------------------
def svg_to_frame(svg: str) -> np.ndarray:
    png_bytes = cairosvg.svg2png(bytestring=svg.encode("utf-8"))
    img = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    return np.array(img)

def render_video(
    script: Script,
    out_path: str,
    width: int,
    height: int,
    fps: int,
    bg: str,
    font_family: str,
    font_weight: str,
    font_size: int,
    line_spacing: float,
    align: str,
    margin_x: int,
    macro_block_size: int,
):
    dur = total_duration(script)
    total_frames = int(round(dur * fps))

    frames = []
    for i in range(total_frames):
        t = i / fps
        svg = render_list_svg(
            script=script,
            t=t,
            width=width,
            height=height,
            bg=bg,
            font_family=font_family,
            font_weight=font_weight,
            font_size=font_size,
            line_spacing=line_spacing,
            align=align,
            margin_x=margin_x,
        )
        frames.append(svg_to_frame(svg))

    imageio.mimsave(
        out_path,
        frames,
        fps=fps,
        codec="libx264",
        macro_block_size=macro_block_size,
        # These ffmpeg params are optional but nice for YouTube:
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart"],
    )

# --------------------------------------------------
# CLI
# --------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Generate a simple text movie from a tiny DSL."
    )
    ap.add_argument("script", nargs="?", help="Path to script text file (DSL).")
    ap.add_argument("-o", "--output", default=DEFAULT_OUT, help="Output .mp4 file.")
    ap.add_argument("--teach", action="store_true", help="Generate a self-explanatory teaching movie.")
    ap.add_argument("--width", type=int, default=DEFAULT_WIDTH)
    ap.add_argument("--height", type=int, default=DEFAULT_HEIGHT)
    ap.add_argument("--fps", type=int, default=DEFAULT_FPS)
    ap.add_argument("--bg", default=DEFAULT_BG, help="Background color (SVG/CSS token).")
    ap.add_argument("--font-family", default=DEFAULT_FONT_FAMILY)
    ap.add_argument("--font-weight", default=DEFAULT_FONT_WEIGHT)
    ap.add_argument("--font-size", type=int, default=DEFAULT_FONT_SIZE)
    ap.add_argument("--line-spacing", type=float, default=1.6, help="Line spacing multiplier.")
    ap.add_argument("--align", choices=["center", "left"], default="center")
    ap.add_argument("--margin-x", type=int, default=120, help="Left margin when --align left.")
    ap.add_argument("--macro-block-size", type=int, default=1,
                    help="Set to 1 to prevent 16px macroblock padding (YouTube is fine with this).")

    args = ap.parse_args()

    if args.teach:
        script = parse_script_text(TEACH_SCRIPT)
    else:
        if not args.script:
            ap.error("Provide a script file path, or use --teach.")
        script = parse_script_file(args.script)

    render_video(
        script=script,
        out_path=args.output,
        width=args.width,
        height=args.height,
        fps=args.fps,
        bg=args.bg,
        font_family=args.font_family,
        font_weight=args.font_weight,
        font_size=args.font_size,
        line_spacing=args.line_spacing,
        align=args.align,
        margin_x=args.margin_x,
        macro_block_size=args.macro_block_size,
    )

    print(f"wrote: {args.output}")

if __name__ == "__main__":
    main()
