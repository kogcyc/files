from D2 import D2, D2line, D2circle, D2svg
import math

p = D2svg(width=2000, height=1300)

# set tbe bottom bracket location

bb = D2()

# construct the seat tube

stc  = bb.polar(180-73,580)
sttt = stc.polar(180-73,20)

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

# calculate position of the rear axle

chainstay_length = 435
bottom_bracket_drop = 90
frac = bottom_bracket_drop / chainstay_length
ang = math.degrees(math.asin(frac))
portion = math.cos(math.radians(ang))
rear_axle_point_x = 0 - (chainstay_length * portion)

rear_axle_point = D2(rear_axle_point_x,bottom_bracket_drop)

# conasruct rear wheel bsd

rear_wheel_circle = D2circle(rear_axle_point,311)
p.add_circle(rear_wheel_circle)

# construct rear dropout

p.add_dot(rear_axle_point,r=17,fill="#fff")

# construct rear dropout slot

slot_out = rear_axle_point.polar(-70,25) 
dropout_slot = D2line(rear_axle_point,slot_out)
p.add_line(dropout_slot,stroke="#5e5c64",stroke_width=10)

# construct rear axle

p.add_dot(rear_axle_point,r=5,fill="#f00")

p.saveas("bike.svg")
