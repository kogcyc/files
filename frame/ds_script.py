from d2stuff import *
a = D2()
b = a.vector_to(350,-73)
c = b.vector_to(68,17)
d = D2Circle(center=c,radius=150)

e = a.vector_to(150,-73)
f = e.vector_to(150,17)

g = a.vector_to(550,-73)
h = e.vector_to(150,17)

i = D2Line().set_attr_two_points(f,h)

intersections = d.intersection_points(i)

intresections
intersections
intersections[0]
intersections[0].line_to(intersections[1])
f.line_to(h)
e.line_to(f)


g.line_to(h)
f.line_to(h)
i = D2Line().set_attr_two_points(f,h)
i
i[0]
intersections = d.intersection_points(i)
intersections[0].line_to(intersections[1])

j = D2Circle(center=intersections[1],radius=150)
intersections[1].circle(150)
intersections[1].circle_at(150)
