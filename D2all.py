import math
import svgwrite

class D2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
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
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        return D2(mid_x, mid_y)
    
    def slope(self):
        if abs(self.p2.x - self.p1.x) < 1e-10:
            return None
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
    
    def __repr__(self):
        return f"D2line({self.p1}, {self.p2})"

class D2circle:
    def __init__(self, center, radius):
        if not isinstance(center, D2):
            raise TypeError("Center must be a D2 instance")
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.center = center.copy()
        self.radius = radius
    
    def intersection_with_line(self, line):
        if not isinstance(line, D2line):
            raise TypeError("Line must be a D2line instance")
        
        # Translate everything so circle is at origin
        p1_x = line.p1.x - self.center.x
        p1_y = line.p1.y - self.center.y
        p2_x = line.p2.x - self.center.x
        p2_y = line.p2.y - self.center.y
        
        # Line vector
        dx = p2_x - p1_x
        dy = p2_y - p1_y
        
        # Coefficients for quadratic equation
        a = dx * dx + dy * dy
        b = 2 * (p1_x * dx + p1_y * dy)
        c = p1_x * p1_x + p1_y * p1_y - self.radius * self.radius
        
        # Discriminant
        discriminant = b * b - 4 * a * c
        
        if discriminant < 0:
            return None
        
        # Find solutions for t
        sqrt_discriminant = math.sqrt(discriminant)
        t1 = (-b - sqrt_discriminant) / (2 * a)
        t2 = (-b + sqrt_discriminant) / (2 * a)
        
        # Check which solutions are within [0, 1]
        solutions = []
        if 0 <= t1 <= 1:
            solutions.append(t1)
        if 0 <= t2 <= 1:
            solutions.append(t2)
        
        if not solutions:
            return None
        
        # Return the intersection point closest to line start
        t = min(solutions)
        intersect_x = line.p1.x + t * dx
        intersect_y = line.p1.y + t * dy
        
        return D2(intersect_x, intersect_y)
    
    def __repr__(self):
        return f"D2circle(center={self.center}, radius={self.radius})"

def create_svg_with_transform_scale(circle, line, intersection_point, filename='geometry_transform.svg'):
    """
    Create an SVG with mathematical coordinates (Y-up) using transform scale
    """
    # Create SVG drawing
    dwg = svgwrite.Drawing(filename, size=('400px', '400px'))
    
    # Add background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='#2c3e50'))
    
    # Create transformation group: translate to center and flip Y-axis
    transform_group = dwg.g(transform="translate(200,200) scale(1,-1)")
    
    # Add coordinate grid (in mathematical coordinates)
    for i in range(-150, 151, 50):
        if i != 0:  # Skip axes
            # Vertical grid lines
            transform_group.add(dwg.line(
                start=(i, -150), end=(i, 150),
                stroke='#34495e', stroke_width=0.5
            ))
            # Horizontal grid lines
            transform_group.add(dwg.line(
                start=(-150, i), end=(150, i),
                stroke='#34495e', stroke_width=0.5
            ))
    
    # Add coordinate axes (in mathematical coordinates)
    transform_group.add(dwg.line(
        start=(-200, 0), end=(200, 0),
        stroke='#7f8c8d', stroke_width=1.5
    ))
    transform_group.add(dwg.line(
        start=(0, -200), end=(0, 200),
        stroke='#7f8c8d', stroke_width=1.5
    ))
    
    # Add circle (in mathematical coordinates)
    transform_group.add(dwg.circle(
        center=(circle.center.x, circle.center.y),
        r=circle.radius,
        stroke='#e74c3c',
        stroke_width=3,
        fill='none',
        opacity=0.8
    ))
    
    # Add center point
    transform_group.add(dwg.circle(
        center=(circle.center.x, circle.center.y),
        r=4,
        fill='#e74c3c'
    ))
    
    # Add line segment (in mathematical coordinates)
    transform_group.add(dwg.line(
        start=(line.p1.x, line.p1.y),
        end=(line.p2.x, line.p2.y),
        stroke='#3498db',
        stroke_width=3
    ))
    
    # Add line endpoints
    transform_group.add(dwg.circle(
        center=(line.p1.x, line.p1.y),
        r=4,
        fill='#3498db'
    ))
    transform_group.add(dwg.circle(
        center=(line.p2.x, line.p2.y),
        r=4,
        fill='#3498db'
    ))
    
    # Add intersection point if it exists
    if intersection_point:
        transform_group.add(dwg.circle(
            center=(intersection_point.x, intersection_point.y),
            r=5,
            fill='#2ecc71',
            stroke='white',
            stroke_width=1
        ))
    
    # Add the transformation group to the drawing
    dwg.add(transform_group)
    
    # Add labels (outside the transformed group so they're not flipped)
    labels_group = dwg.g(style="font-family: Arial, sans-serif; font-size: 12px;")
    
    # Coordinate labels
    labels_group.add(dwg.text("+X", insert=(380, 210), fill='#bdc3c7'))
    labels_group.add(dwg.text("-X", insert=(10, 210), fill='#bdc3c7'))
    labels_group.add(dwg.text("+Y", insert=(190, 20), fill='#bdc3c7'))
    labels_group.add(dwg.text("-Y", insert=(190, 380), fill='#bdc3c7'))
    
    # Title
    labels_group.add(dwg.text(
        "Circle-Line Intersection (Mathematical Coordinates)",
        insert=(10, 30),
        fill='#ecf0f1',
        font_size=14,
        font_weight='bold'
    ))
    
    # Data labels
    labels_group.add(dwg.text(
        f"Circle: center({circle.center.x}, {circle.center.y}), radius={circle.radius}",
        insert=(10, 50),
        fill='#e74c3c'
    ))
    labels_group.add(dwg.text(
        f"Line: ({line.p1.x}, {line.p1.y}) to ({line.p2.x}, {line.p2.y})",
        insert=(10, 65),
        fill='#3498db'
    ))
    
    if intersection_point:
        labels_group.add(dwg.text(
            f"Intersection: ({intersection_point.x:.2f}, {intersection_point.y:.2f})",
            insert=(10, 80),
            fill='#2ecc71',
            font_weight='bold'
        ))
    else:
        labels_group.add(dwg.text(
            "No intersection found",
            insert=(10, 80),
            fill='#e67e22'
        ))
    
    dwg.add(labels_group)
    
    # Save the SVG
    dwg.save()
    print(f"SVG saved as {filename}")

# Test the script
if __name__ == "__main__":
    # Create test objects
    circle = D2circle(D2(0, 0), 100)
    line = D2line(D2(-20, 130), D2(50, 70))
    
    # Find intersection
    intersection = circle.intersection_with_line(line)
    
    print("Circle:", circle)
    print("Line:", line)
    print("Intersection:", intersection)
    
    if intersection:
        # Verify the intersection point is on the circle
        distance = circle.center.distance_to(intersection)
        print(f"Distance from center to intersection: {distance:.6f} (should be ~{circle.radius})")
    
    # Create SVG with mathematical coordinates
    create_svg_with_transform_scale(circle, line, intersection, "circle_line_intersection.svg")
    
    print("\nSVG created with mathematical coordinates (Y-up)!")
