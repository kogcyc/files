import math

class D2:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

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

def radius_and_circumfrence_teeth(t):
    circumfrence = t * 12.7
    diameter = circumfrence / math.pi
    radius = diameter / 2.0
    return radius,circumfrence

def calc_angle(big_radius,little_radius,chainstay):
    delta = big_radius - little_radius
    angle = math.degrees(math.atan(delta/chainstay))
    return(angle)

big_r,big_c = radius_and_circumfrence_teeth(34)
little_r,little_c = radius_and_circumfrence_teeth(15)
chainstay = 395

angle = calc_angle(big_r,little_r,chainstay)
print(angle)

p1 = D2().vector_to(little_r,(90+angle))
print(p1)

p2 = D2(chainstay,0).vector_to(big_r,(90+angle))
side = abs(p1.distance_to(p2))
print(side)

little_arc = (180 - angle*2.0) / 360.0
big_arc = (360.0 - little_arc) / 360.0

little_bit = little_c * little_arc
big_bit = big_c * big_arc

print(little_bit)
print(big_bit)

total = (side*2 + little_bit + big_bit)/12.7

print(total)
