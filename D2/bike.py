from D2 import D2, D2line, D2circle, D2svg
import math

p = D2svg(width=2000, height=1300)

# set tbe bottom bracket location

bb = D2()

# construct the seat tube

stc  = bb.polar(117,580)
sttt = stc.polar(117,20)

stline = D2line(bb,stc)
p.add_line(stline,stroke="#fff",stroke_width=28)

sttline = D2line(sttt,stc)
p.add_line(sttline,stroke="#fff",stroke_width=30,stroke_linecap="square")

# construct the top tube

httc = stc.polar(0,570)

ttline = D2line(stc,httc)
p.add_line(ttline,stroke="#fff",stroke_width=25)

# construct the bottom bracket

p.add_dot(bb,r=21,fill="#fff")
p.add_dot(bb,r=17,fill="#5e5c64")

# make a rear dropout

chainstay_length = 435.0
bottom_bracket_drop = 90.0
angle = math.degrees(math.asin(bottom_bracket_drop / chainstay_length))
axle_point = D2((chainstay_length*math.cos(angle)) * -1.0, bottom_bracket_drop)
print(axle_point)
p.add_dot(axle_point,r=5,fill="#ace")
rear_wheel_circle = D2circle(axle_point,322)
p.add_circle(rear_wheel_circle)

p.saveas("bike.svg")
