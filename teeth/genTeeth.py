from realHYP import origin_to_vertex
from D2 import *
from svgLIBmm import *
from sys import argv

def generate_sprocket_svg(teeth=35, tangle=32, tlength=4, ttop=4, output_fn="teeth.svg"):
    # Calculate derived parameters
    d2v = origin_to_vertex(teeth)
    ttangle = 360.0 / teeth
    roller_rad = 4  # Approximation of 5/32 * 25.4 in mm
    origin = D2()

    # Precompute key points
    pr = [None] * 4
    pr[1] = D2().vector(roller_rad, 270 - tangle)
    pr[0] = pr[1].vector(tlength, -tangle)
    pr[2] = pr[1].mirror_x()
    pr[3] = pr[0].mirror_x()

    # Calculate ellipse radius for the sprocket path
    p3_pre = pr[3].translate(d2v, 0.0).rotate(origin, -ttangle)
    ang, ellipse_y = p3_pre.angle_and_length_to(pr[0].translate(d2v, 0.0))
    ellipse_y_rad = ellipse_y / 2

    # Build the SVG path
    svg_path = [f'<path d="M {p3_pre.x} {p3_pre.y}']

    for u in range(teeth):
        p0 = pr[0].translate(d2v, 0.0).rotate(origin, u * ttangle)
        p1 = pr[1].translate(d2v, 0.0).rotate(origin, u * ttangle)
        p2 = pr[2].translate(d2v, 0.0).rotate(origin, u * ttangle)
        p3 = pr[3].translate(d2v, 0.0).rotate(origin, u * ttangle)

        svg_path.append(f' A {ellipse_y_rad * ttop} {ellipse_y_rad * ttop} 0 0 1 {p0.x} {p0.y}')
        svg_path.append(f' L {p1.x} {p1.y}')
        svg_path.append(f' A {roller_rad} {roller_rad} 0 0 0 {p2.x} {p2.y}')
        svg_path.append(f' L {p3.x} {p3.y}')

    svg_path.append(' Z" />')
    svgMID = ''.join(svg_path)

    svgMID = svgMID + '<circle cx="0" cy="0" r="3" fill="#f00" stroke="none"/>'

    # Write to file
    output_path = f'./geeqie/{output_fn}'
    with open(output_path, 'w') as ff:
        ff.write(makeSVG(svgMID))

if __name__ == "__main__":
    try:
        teeth = int(argv[1])
    except (IndexError, ValueError):
        teeth = 35

    try:
        tangle = int(argv[2])
    except (IndexError, ValueError):
        tangle = 32

    try:
        tlength = int(argv[3])
    except (IndexError, ValueError):
        tlength = 4

    try:
        ttop = int(argv[4])
    except (IndexError, ValueError):
        ttop = 4

    try:
        output_fn = argv[0] + ".svg"
    except IndexError:
        output_fn = "teeth.svg"

    generate_sprocket_svg(teeth, tangle, tlength, ttop, output_fn)

