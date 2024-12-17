import math

# sudo apt install xclip
from subprocess import Popen, PIPE

def copy_clipboard(msg):
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))

# Copy some text to the clipboard
# copy_clipboard('This is a test')

def D2SVG_line(p1,p2):
    line = f'<line x1="{p1.x}" y1="{p1.y}" x2="{p2.x}" y2="{p2.y}" stroke="#fff" stroke-width="5" />'
    copy_clipboard(line)
    return line
def D2SVG_circle(p,r):
    circle = f'<circle cx="{p.x}" cy="{p.y}" r="{r}" stroke="#fff" stroke-width="5" fill="none" />'
    copy_clipboard(circle)
    return circle

class D2:
    def __init__(self, x=0.0, y=0.0):
        self.x = round(float(x),3)
        self.y = round(float(y),3)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    def angle_to(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        return math.degrees(math.atan2(dy, dx))

    def vector_to(self, distance, direction):
        angle = math.radians(direction)
        dx = distance * math.cos(angle)
        dy = distance * math.sin(angle)
        return D2(self.x + dx, self.y + dy)

class D2Line:
    def __init__(self, m=1.0, b=D2(0.0, -1.0), xi=D2(1.0, 0.0)):
        self.m = m
        self.b = b
        self.xi = xi

    def set_attr_two_points(self, p1=None, p2=None):
        if p1 is None or p2 is None:
            raise ValueError("Two points must be provided")
        if p1.x == p2.x:
            m = float('inf')
            b = None
            xi = D2(p1.x, 0.0)
        else:
            m = (p2.y - p1.y) / (p2.x - p1.x)
            b = D2(0.0, p1.y - m * p1.x)
            xi = D2((-b.y) / m, 0.0)
        return D2Line(m=m, b=b, xi=xi)

    def set_attr_slope_intercept(self, m, b):
        return D2Line(m=m, b=b, xi=D2((-b.y) / m, 0.0))

    def set_attr_point_slope(self, p, m):
        b = D2(0.0, p.y - m * p.x)
        return D2Line(m=m, b=b, xi=D2((-b.y) / m, 0.0))

    def point_at_x(self, x):
        if self.m == float('inf'):
            return D2(self.xi.x, x)
        else:
            y = self.m * x + self.b.y
            return D2(x, y)

    def point_at_y(self, y):
        if self.m == 0:
            return D2(y, self.b.y)
        elif self.m == float('inf'):
            return D2(self.xi.x, y)
        else:
            x = (y - self.b.y) / self.m
            return D2(x, y)

    def intersection_with(self, other_line):
        if self.m == other_line.m:
            raise ValueError("Lines are parallel and do not intersect")

        if self.m == float('inf'):
            x_intersect = self.xi.x
            y_intersect = other_line.m * x_intersect + other_line.b.y
        elif other_line.m == float('inf'):
            x_intersect = other_line.xi.x
            y_intersect = self.m * x_intersect + self.b.y
        else:
            x_intersect = (other_line.b.y - self.b.y) / (self.m - other_line.m)
            y_intersect = self.m * x_intersect + self.b.y

        return D2(x_intersect,y_intersect)


class D2Circle:
    def __init__(self, center=D2(), radius=1.0):
        self.center = center  # Center point of the circle (D2 instance)
        self.radius = float(radius)  # Radius of the circle

    def __str__(self):
        return f"Circle with center {self.center} and radius {self.radius}"

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def intersection_points(self, line):
        """
        Find the intersection points between the circle and a D2line.

        Args:
            line (D2line): The D2line to find intersection points with.

        Returns:
            List[D2]: A list of D2 points representing the intersection points.
        """
        intersection_points = []

        # Circle center coordinates
        cx, cy = self.center.x, self.center.y

        # Line slope, intercept, and xi coordinates
        m = line.m
        b = line.b
        xi = line.xi.x

        if m == float('inf'):
            # Special case: vertical line
            # Calculate the x-coordinate of the intersection points
            dx = self.radius
            x1 = xi - dx
            x2 = xi + dx

            # Calculate the y-coordinates of the intersection points
            y1 = cy - math.sqrt(self.radius**2 - dx**2)
            y2 = cy + math.sqrt(self.radius**2 - dx**2)

            intersection_points.append(D2(x1, y1))
            intersection_points.append(D2(x2, y2))
        else:
            # General case
            A = 1 + m**2
            B = 2 * (m * (b.y - cy) - cx)
            C = cx**2 + (b.y - cy)**2 - self.radius**2

            # Calculate the discriminant
            discriminant = B**2 - 4 * A * C

            if discriminant >= 0:
                # Calculate the x-coordinates of the intersection points
                x1 = (-B + math.sqrt(discriminant)) / (2 * A)
                x2 = (-B - math.sqrt(discriminant)) / (2 * A)

                # Calculate the corresponding y-coordinates
                y1 = m * x1 + b.y
                y2 = m * x2 + b.y

                intersection_points.append(D2(x1, y1))
                intersection_points.append(D2(x2, y2))

        return intersection_points

# Example usage:
#center_point = D2(2.0, 3.0)
#my_circle = D2Circle(center=center_point, radius=5.0)

#print(my_circle)  # Print circle information

#line = D2Line(m=2.0, D2=b(0.0, 1.0), xi=D2(1.0, 0.0))
#intersections = my_circle.intersection_points(line)
#for point in intersections:
#    print(f"Intersection point: {point}")


