#!/usr/bin/env python3
"""
chain_svg_fitC.py

Given:
  small_teeth  big_teeth  C_min_mm

Find:
  Smallest center distance ≥ C_min that uses an EVEN integer link count.

Outputs SVG of the resulting geometry.
"""

import math
import argparse
from dataclasses import dataclass


@dataclass
class Pt:
    x: float
    y: float


# ---------- CHAIN GEOMETRY ----------

def pitch_radius(p, T):
    return p / (2 * math.sin(math.pi / T))


def ideal_links(T1, T2, C, p):
    Cp = C / p
    return (
        2 * Cp
        + (T1 + T2) / 2
        + (T2 - T1) ** 2 / (4 * math.pi ** 2 * Cp)
    )


def center_from_links(T1, T2, N, p):
    B = (T1 + T2) / 2 - N
    D = (T2 - T1) ** 2 / (4 * math.pi ** 2)
    Cp = (-B + math.sqrt(B * B - 8 * D)) / 4
    return Cp * p


def next_even_up(x):
    n = math.ceil(x)
    if n % 2:
        n += 1
    return n


# ---------- SVG HELPERS ----------

def arc_path(a, b, r, large, sweep):
    return f"M {a.x:.3f},{a.y:.3f} A {r:.3f},{r:.3f} 0 {large} {sweep} {b.x:.3f},{b.y:.3f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("small", type=int)
    ap.add_argument("big", type=int)
    ap.add_argument("Cmin", type=float)
    ap.add_argument("--pitch", type=float, default=12.7)
    ap.add_argument("--out", default="chain.svg")
    args = ap.parse_args()

    Ts, Tl = args.small, args.big
    C0 = args.Cmin
    p = args.pitch

    # Ensure Tl ≥ Ts
    if Tl < Ts:
        Ts, Tl = Tl, Ts

    # --- STEP 1: Ideal link count at C0
    N_ideal = ideal_links(Ts, Tl, C0, p)

    # --- STEP 2: Next even link count
    N = next_even_up(N_ideal)

    # --- STEP 3: Exact center distance for that N
    C = center_from_links(Ts, Tl, N, p)

    # Radii
    Rs = pitch_radius(p, Ts)
    Rl = pitch_radius(p, Tl)

    alfa = math.asin((Rl - Rs) / C)

    Csx, Clx = -C/2, C/2

    # Tangency points
    small_top = Pt(Csx + Rs*math.sin(alfa),  Rs*math.cos(alfa))
    small_bot = Pt(Csx + Rs*math.sin(alfa), -Rs*math.cos(alfa))

    big_top   = Pt(Clx - Rl*math.sin(alfa),  Rl*math.cos(alfa))
    big_bot   = Pt(Clx - Rl*math.sin(alfa), -Rl*math.cos(alfa))

    # Flip Y for SVG
    def svg(pt): return Pt(pt.x, -pt.y)

    s_top, s_bot = svg(small_top), svg(small_bot)
    b_top, b_bot = svg(big_top), svg(big_bot)

    # SVG arcs using YOUR traversal rule
    big_arc = arc_path(b_top, b_bot, Rl, large=1, sweep=1)
    small_arc = arc_path(s_bot, s_top, Rs, large=0, sweep=1)

    # viewBox adjusters for background rect
    vb_x = Csx - Rl - 40
    vb_y = -Rl - 40
    vb_w = C + 2*Rl + 80
    vb_h = 2*Rl + 80

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
    <svg xmlns="http://www.w3.org/2000/svg"
    width="800" height="400"
    viewBox="{vb_x} {vb_y} {vb_w} {vb_h}">

    <rect x="{vb_x}" y="{vb_y}" width="{vb_w}" height="{vb_h}"
        fill="#05060a"/>

    <path d="{big_arc}" fill="none" stroke="lime" stroke-width="14"/>
    <path d="{small_arc}" fill="none" stroke="red" stroke-width="14"/>

    <line x1="{s_top.x}" y1="{s_top.y}" x2="{b_top.x}" y2="{b_top.y}"
        stroke="orange" stroke-width="14"/>

    <line x1="{b_bot.x}" y1="{b_bot.y}" x2="{s_bot.x}" y2="{s_bot.y}"
        stroke="blue" stroke-width="14"/>
    </svg>
    """

    with open(args.out, "w") as f:
        f.write(svg)

    print("\n=== Chain Fit Report ===")
    print(f"Small teeth      : {Ts}")
    print(f"Large teeth      : {Tl}")
    print(f"Pitch            : {p} mm")
    print(f"Requested C_min  : {C0:.3f} mm")
    print(f"Ideal links      : {N_ideal:.3f}")
    print(f"Chosen links     : {N} (even)")
    print(f"Resulting C      : {C:.3f} mm")
    print(f"Growth needed    : {C - C0:+.3f} mm")
    print("========================")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
