import math

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
