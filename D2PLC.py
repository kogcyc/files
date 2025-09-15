import math

class D2:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def translate(self, dx, dy):
        return D2(self.x + dx, self.y + dy)
    
    def polar(self, angle_degrees, distance):
        """Return a new point at polar coordinates relative to this point."""
        angle_radians = math.radians(angle_degrees)
        dx = distance * math.cos(angle_radians)
        dy = distance * math.sin(angle_radians)
        return self.translate(dx, dy)
    
    def copy(self):
        return D2(self.x, self.y)
    
    def __repr__(self):
        return f"D2({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Check if two points are equal."""
        if not isinstance(other, D2):
            return False
        return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10


class D2line:
    
    def __init__(self, point1, point2):
        """
        Initialize a line with two D2 points.
        
        Args:
            point1 (D2): First point defining the line
            point2 (D2): Second point defining the line
        """
        if not isinstance(point1, D2) or not isinstance(point2, D2):
            raise TypeError("Both arguments must be D2 instances")
        
        self.p1 = point1.copy()
        self.p2 = point2.copy()
    
    def length(self):
        """Return the length of the line segment."""
        return self.p1.distance_to(self.p2)
    
    def midpoint(self):
        """Return the midpoint of the line segment."""
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        return D2(mid_x, mid_y)
    
    def slope(self):
        """Return the slope of the line (rise/run). Returns None for vertical lines."""
        if abs(self.p2.x - self.p1.x) < 1e-10:
            return None  # Vertical line
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
    
    def angle(self):
        """Return the angle of the line in degrees (0-360) from horizontal."""
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        
        if abs(dx) < 1e-10:  # Vertical line
            return 90 if dy > 0 else 270
        
        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)
        
        # Normalize to 0-360 degrees
        return angle_deg % 360
    
    def is_parallel_to(self, other_line):
        """Check if this line is parallel to another line."""
        if not isinstance(other_line, D2line):
            raise TypeError("Argument must be a D2line instance")
        
        slope1 = self.slope()
        slope2 = other_line.slope()
        
        # Both vertical or both have same slope (with tolerance)
        if slope1 is None and slope2 is None:
            return True
        if slope1 is None or slope2 is None:
            return False
        return abs(slope1 - slope2) < 1e-10
    
    def is_perpendicular_to(self, other_line):
        """Check if this line is perpendicular to another line."""
        if not isinstance(other_line, D2line):
            raise TypeError("Argument must be a D2line instance")
        
        slope1 = self.slope()
        slope2 = other_line.slope()
        
        # Handle cases where one or both lines are vertical/horizontal
        if slope1 is None:  # This line is vertical
            return abs(slope2) < 1e-10  # Other line should be horizontal
        if slope2 is None:  # Other line is vertical
            return abs(slope1) < 1e-10  # This line should be horizontal
        
        # Check if slopes are negative reciprocals
        return abs(slope1 * slope2 + 1) < 1e-10
    
    def distance_to_point(self, point):
        """Return the shortest distance from this line to a point."""
        if not isinstance(point, D2):
            raise TypeError("Point must be a D2 instance")
        
        # Using the formula for distance from point to line
        numerator = abs((self.p2.y - self.p1.y) * point.x - 
                       (self.p2.x - self.p1.x) * point.y + 
                       self.p2.x * self.p1.y - self.p2.y * self.p1.x)
        denominator = self.length()
        
        return numerator / denominator if denominator != 0 else 0
    
    def intersection(self, other_line):
        """
        Find the intersection point of this line with another line.
        
        Args:
            other_line (D2line): The other line to find intersection with
            
        Returns:
            D2: The intersection point, or None if lines are parallel or coincident
        """
        if not isinstance(other_line, D2line):
            raise TypeError("Argument must be a D2line instance")
        
        # Check if lines are parallel
        if self.is_parallel_to(other_line):
            return None
        
        # Line 1: points A, B
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        
        # Line 2: points C, D
        x3, y3 = other_line.p1.x, other_line.p1.y
        x4, y4 = other_line.p2.x, other_line.p2.y
        
        # Calculate determinant
        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        
        if abs(det) < 1e-10:  # Lines are parallel or coincident
            return None
        
        # Calculate intersection coordinates
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / det
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / det
        
        # Check if intersection point lies within both line segments (optional)
        # If you want to find intersection of infinite lines, remove this check
        if 0 <= t <= 1 and 0 <= u <= 1:
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            return D2(x, y)
        
        return None  # Intersection exists but not within segments
    
    def translate(self, dx, dy):
        """Return a new line translated by dx, dy."""
        return D2line(self.p1.translate(dx, dy), self.p2.translate(dx, dy))
    
    def copy(self):
        """Return a copy of this line."""
        return D2line(self.p1.copy(), self.p2.copy())
    
    def __repr__(self):
        return f"D2line({self.p1}, {self.p2})"
    
    def __eq__(self, other):
        """Check if two lines are equal (have the same endpoints)."""
        if not isinstance(other, D2line):
            return False
        return (self.p1 == other.p1 and self.p2 == other.p2) or \
               (self.p1 == other.p2 and self.p2 == other.p1)


class D2circle:
    
    def __init__(self, center, radius):
        """
        Initialize a circle with a center point and radius.
        
        Args:
            center (D2): Center point of the circle
            radius (float): Radius of the circle (must be non-negative)
        """
        if not isinstance(center, D2):
            raise TypeError("Center must be a D2 instance")
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        
        self.center = center.copy()
        self.radius = radius
    
    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2
    
    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.radius
    
    def contains_point(self, point):
        """Check if a point is inside or on the circle."""
        if not isinstance(point, D2):
            raise TypeError("Point must be a D2 instance")
        
        return self.center.distance_to(point) <= self.radius
    
    def translate(self, dx, dy):
        """Return a new circle translated by dx, dy."""
        return D2circle(self.center.translate(dx, dy), self.radius)
    
    def scale(self, factor):
        """Return a new circle scaled by the given factor."""
        if factor < 0:
            raise ValueError("Scale factor must be non-negative")
        return D2circle(self.center.copy(), self.radius * factor)
    
    def copy(self):
        """Return a copy of this circle."""
        return D2circle(self.center.copy(), self.radius)
    
    def intersection_with_line(self, line):
        """
        Find the intersection point(s) between this circle and a line segment.
        Returns the first intersection point found along the line segment from p1 to p2,
        or None if no intersection exists.
        """
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
            return None  # No real solutions, no intersection
        
        # Find solutions for t (parameter along line segment)
        sqrt_discriminant = math.sqrt(discriminant)
        t1 = (-b - sqrt_discriminant) / (2 * a)
        t2 = (-b + sqrt_discriminant) / (2 * a)
        
        # Check which solutions are within [0, 1] (on the line segment)
        solutions = []
        if 0 <= t1 <= 1:
            solutions.append(t1)
        if 0 <= t2 <= 1:
            solutions.append(t2)
        
        if not solutions:
            return None  # No intersection within line segment
        
        # Return the intersection point closest to line start (smallest t)
        t = min(solutions)
        intersect_x = line.p1.x + t * dx
        intersect_y = line.p1.y + t * dy
        
        return D2(intersect_x, intersect_y)
    
    def __repr__(self):
        return f"D2circle(center={self.center}, radius={self.radius})"
    
    def __eq__(self, other):
        """Check if two circles are equal."""
        if not isinstance(other, D2circle):
            return False
        return self.center == other.center and abs(self.radius - other.radius) < 1e-10
