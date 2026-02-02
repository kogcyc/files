import cairosvg
import imageio
import numpy as np
from PIL import Image
import io

# --------------------------------------------------
# Configuration
# --------------------------------------------------
WIDTH, HEIGHT = 1920, 1088
FPS = 24

FONT_FAMILY = "DejaVu Sans Bold"
FONT_WEIGHT = "normal"
FONT_SIZE = 72

TEXTS = [
    "hello",
    "this is text in the form of a movie",
    "for people who don't like to read",
    "like me",
]

FADE_IN  = 0.75   # seconds
HOLD     = 1.5
FADE_OUT = 0.75

OUTPUT = "textmovie.mp4"

# --------------------------------------------------
# Helpers
# --------------------------------------------------
def clamp(x):
    return max(0.0, min(1.0, x))

def opacity_at(t):
    if t < FADE_IN:
        return clamp(t / FADE_IN)
    elif t < FADE_IN + HOLD:
        return 1.0
    elif t < FADE_IN + HOLD + FADE_OUT:
        return clamp(1 - (t - FADE_IN - HOLD) / FADE_OUT)
    else:
        return 0.0

def render_svg(text, opacity):
    return f'''
    <svg width="{WIDTH}" height="{HEIGHT}"
         xmlns="http://www.w3.org/2000/svg">

      <rect width="100%" height="100%" fill="black"/>

      <text x="50%" y="50%"
            font-family="{FONT_FAMILY}"
            font-weight="{FONT_WEIGHT}"
            font-size="{FONT_SIZE}"
            fill="white"
            fill-opacity="{opacity:.3f}"
            text-anchor="middle"
            dominant-baseline="middle">
        {text}
      </text>

    </svg>
    '''

# --------------------------------------------------
# Frame generation
# --------------------------------------------------
frames = []

card_duration = FADE_IN + HOLD + FADE_OUT
frames_per_card = int(card_duration * FPS)

for text in TEXTS:
    for i in range(frames_per_card):
        t = i / FPS
        opacity = opacity_at(t)

        svg = render_svg(text, opacity)
        png = cairosvg.svg2png(bytestring=svg.encode())
        img = Image.open(io.BytesIO(png))

        frames.append(np.array(img))

# --------------------------------------------------
# Write video
# --------------------------------------------------
imageio.mimsave(
    OUTPUT,
    frames,
    fps=FPS,
    codec="libx264",
)
