import math
import svgwrite


class D2:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def distance_to(self, other):
        """Euclidean distance between two points."""
        return math.hypot(self.x - other.x, self.y - other.y)

    def translate(self, dx, dy):
        return D2(self.x + dx, self.y + dy)

    def polar(self, angle_degrees, distance):
        angle_radians = math.radians(angle_degrees)
        dx = distance * math.cos(angle_radians)
        dy = distance * math.sin(angle_radians)
        return self.translate(dx, dy)

    def copy(self):
        return D2(self.x, self.y)

    def __repr__(self):
        return f"D2({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, D2):
            return False
        return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10


class D2line:
    def __init__(self, point1, point2):
        if not isinstance(point1, D2) or not isinstance(point2, D2):
            raise TypeError("Both arguments must be D2 instances")
        self.p1 = point1.copy()
        self.p2 = point2.copy()

    def length(self):
        return self.p1.distance_to(self.p2)

    def midpoint(self):
        return D2((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)

    def slope(self):
        if abs(self.p2.x - self.p1.x) < 1e-10:
            return None
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def intersect(self, other):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = other.p1.x, other.p1.y
        x4, y4 = other.p2.x, other.p2.y

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None  # Parallel or coincident

        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - 
              (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - 
              (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

        return D2(px, py)



    def __repr__(self):
        return f"D2line({self.p1}, {self.p2})"


class D2circle:
    def __init__(self, center, radius):
        if not isinstance(center, D2):
            raise TypeError("Center must be a D2 instance")
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.center = center.copy()
        self.radius = float(radius)

    def intersection_with_line(self, line):
        if not isinstance(line, D2line):
            raise TypeError("Line must be a D2line instance")

        # Translate so circle is at origin
        p1_x = line.p1.x - self.center.x
        p1_y = line.p1.y - self.center.y
        p2_x = line.p2.x - self.center.x
        p2_y = line.p2.y - self.center.y

        dx = p2_x - p1_x
        dy = p2_y - p1_y

        a = dx * dx + dy * dy
        b = 2 * (p1_x * dx + p1_y * dy)
        c = p1_x * p1_x + p1_y * p1_y - self.radius * self.radius

        intersections = []

        # Degenerate case: line points coincide (a ≈ 0)
        if abs(a) < 1e-12:
            dist = math.hypot(p1_x, p1_y)
            if abs(dist - self.radius) < 1e-10:
                intersections.append(line.p1.copy())  # Point lies on the circle
            return intersections  # [] if not on

        # Quadratic discriminant
        discriminant = b * b - 4 * a * c
        if discriminant < -1e-12:
            return intersections  # empty list

        if discriminant < 0:
            discriminant = 0  # Clamp small negative to 0
        sqrt_disc = math.sqrt(discriminant)

        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)

        for t in (t1, t2):
            if 0 <= t <= 1:
                x = line.p1.x + t * dx
                y = line.p1.y + t * dy
                intersections.append(D2(x, y))

        return intersections

    def __repr__(self):
        return f"D2circle(center={self.center}, radius={self.radius})"

class D2svg:
    def __init__(self, width=400, height=400, units=None):
        """
        width, height: numbers
        units: None (default) or string like 'mm'
        """
        size = (f"{width}{units or ''}", f"{height}{units or ''}")
        self.dwg = svgwrite.Drawing(size=size)
        # Background rect (optional, matches your boilerplate)
        self.dwg.add(self.dwg.rect(insert=(0, 0), size=size, fill="#5e5c64"))

        # Main group with coordinate transform (center + flip Y)
        self.group = self.dwg.g(
            transform=f"translate({width/2},{height/2}) scale(1,-1)"
        )
        self.dwg.add(self.group)

    def add_line(self, line, **style):
        """Add a line from a D2line"""
        default_style = dict(
            stroke="white", stroke_width=2, fill="none", stroke_linecap="round"
        )
        default_style.update(style)
        self.group.add(
            self.dwg.line(
                start=(line.p1.x, line.p1.y),
                end=(line.p2.x, line.p2.y),
                **default_style,
            )
        )

    def add_trapezoid(self, base_line, width_one, width_two, centered=True, **style):
        """
        Add a trapezoid given a baseline (D2line) and two widths.

        width_one: trapezoid thickness at base_line.p1
        width_two: trapezoid thickness at base_line.p2
        centered: if True, baseline is the midline (two parallel edges on both sides).
                  if False (default), baseline is one edge, offset outward.
        """
        if not isinstance(base_line, D2line):
            raise TypeError("base_line must be a D2line")

        # Direction vector of baseline
        dx = base_line.p2.x - base_line.p1.x
        dy = base_line.p2.y - base_line.p1.y
        length = math.hypot(dx, dy)
        if length < 1e-12:
            raise ValueError("Baseline has zero length")

        # Unit perpendicular (rotate (dx,dy) by 90°)
        perp_x = -dy / length
        perp_y = dx / length

        if centered:
            # Half-offsets in both directions
            p1_offset_pos = D2(base_line.p1.x + perp_x * (width_one / 2),
                               base_line.p1.y + perp_y * (width_one / 2))
            p2_offset_pos = D2(base_line.p2.x + perp_x * (width_two / 2),
                               base_line.p2.y + perp_y * (width_two / 2))
            p1_offset_neg = D2(base_line.p1.x - perp_x * (width_one / 2),
                               base_line.p1.y - perp_y * (width_one / 2))
            p2_offset_neg = D2(base_line.p2.x - perp_x * (width_two / 2),
                               base_line.p2.y - perp_y * (width_two / 2))
            points = [
                (p1_offset_neg.x, p1_offset_neg.y),
                (p2_offset_neg.x, p2_offset_neg.y),
                (p2_offset_pos.x, p2_offset_pos.y),
                (p1_offset_pos.x, p1_offset_pos.y),
            ]
        else:
            # Offset in +perpendicular direction only
            p1_offset = D2(base_line.p1.x + perp_x * width_one,
                           base_line.p1.y + perp_y * width_one)
            p2_offset = D2(base_line.p2.x + perp_x * width_two,
                           base_line.p2.y + perp_y * width_two)
            points = [
                (base_line.p1.x, base_line.p1.y),
                (base_line.p2.x, base_line.p2.y),
                (p2_offset.x, p2_offset.y),
                (p1_offset.x, p1_offset.y),
            ]

        default_style = dict(fill="none", stroke="white", stroke_width=2)
        default_style.update(style)
        self.group.add(self.dwg.polygon(points, **default_style))

    def add_circle(self, circle, **style):
        """Add a circle from a D2circle"""
        default_style = dict(stroke="white", stroke_width=2, fill="none")
        default_style.update(style)
        self.group.add(
            self.dwg.circle(
                center=(circle.center.x, circle.center.y), r=circle.radius, **default_style
            )
        )

    def add_dot(self, point, r=3, **style):
        """
        Add a small filled circle (syntactic sugar for add_circle).
        point: D2 instance
        r: dot radius (default=3)
        """
        circle = D2circle(point, r)
        default_style = dict(fill="red", stroke="none")
        default_style.update(style)
        self.add_circle(circle, **default_style)

    def add_quad_bezier(self, start, control, end, **style):
        """
        Add a quadratic Bézier curve from start -> end with control point.
        start, control, end: D2 instances
        """
        if not all(isinstance(pt, D2) for pt in (start, control, end)):
            raise TypeError("start, control, and end must be D2 instances")

        path_data = [
            f"M {start.x},{start.y}",
            f"Q {control.x},{control.y} {end.x},{end.y}"
        ]
        default_style = dict(stroke="white", stroke_width=2, fill="none")
        default_style.update(style)
        self.group.add(self.dwg.path(d=" ".join(path_data), **default_style))

    def saveas(self, filename):
        self.dwg.saveas(filename)

