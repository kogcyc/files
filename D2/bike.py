# echo bike.py | entr -r python3 bike.py

from D2 import D2, D2line, D2circle, D2svg
import math

p = D2svg(width=2000, height=1300)

sta = 73 # seat tube angle
stl = 620 # seat tube length
ste = 20 # seat tube extension above the top tube center
ttl = 0.5 * stl + 275
print(ttl)

# set tbe bottom bracket location

bb = D2()

# construct the seat tube

stttc  = bb.polar(180-sta,stl)
sttt = stttc.polar(180-sta,20)

stline = D2line(bb,stttc)
p.add_line(stline,stroke="#fff",stroke_width=28)

sttline = D2line(sttt,stttc)
p.add_line(sttline,stroke="#fff",stroke_width=30,stroke_linecap="square")

# construct the top tube

httc = stttc.polar(0,ttl)

ttline = D2line(stttc,httc)
p.add_line(ttline,stroke="#fff",stroke_width=25)

# make a rear dropout

# calculate position of the rear axle

chainstay_length = 435
bottom_bracket_drop = 90
frac = bottom_bracket_drop / chainstay_length
ang = math.degrees(math.asin(frac))
portion = math.cos(math.radians(ang))
rear_axle_point_x = 0 - (chainstay_length * portion)

rear_axle_point = D2(rear_axle_point_x,bottom_bracket_drop)

# construct rear tire 

rear_tire_circle = D2circle(rear_axle_point,584/2+19)
p.add_circle(rear_tire_circle,stroke="#222",stroke_width=40)
rear_sidewall_circle = D2circle(rear_axle_point,584/2+10)
p.add_circle(rear_sidewall_circle,stroke="#5f4433",stroke_width=20)

# construct rear wheel bsd

rear_wheel_circle = D2circle(rear_axle_point,584/2-3)
p.add_circle(rear_wheel_circle)

# construct rear dropout

p.add_dot(rear_axle_point,r=17,fill="#fff")

# construct rear dropout slot

slot_out = rear_axle_point.polar(-70,25) 
dropout_slot = D2line(rear_axle_point,slot_out)
p.add_line(dropout_slot,stroke="#5e5c64",stroke_width=10)

# construct rear axle

p.add_dot(rear_axle_point,r=5,fill="#f00")

# construct chainstay

base = D2line(bb, rear_axle_point.translate(13.6,-6.9))
p.add_trapezoid(base, width_one=28, width_two=12, fill="#fff")

# construct seatstay

base = D2line(stttc, rear_axle_point.translate(-7,9))
p.add_trapezoid(base, width_one=16, width_two=10, fill="#fff")

# construct the bottom bracket

p.add_dot(bb,r=21,fill="#fff")
p.add_dot(bb,r=17,fill="#5e5c64")

p.add_line(D2line(httc,httc.polar(107,40)),stroke="#fff",stroke_width=32,stroke_linecap="square")

fork_contrux_line = D2line(httc,httc.polar(-73,555))
p.add_line(fork_contrux_line,stroke="#0f0",stroke_width=2)

axle_contrux_line = D2line(D2(200,90),D2(900,90))
p.add_line(axle_contrux_line,stroke="#777",stroke_width=2)

ppoint = fork_contrux_line.intersect(axle_contrux_line)
p.add_dot(ppoint,r=6,fill="#000")


opp = 68 * math.tan(math.radians(17))
hyp = 68 / math.cos(math.radians(17))

apoint = ppoint.polar(0,hyp)
p.add_dot(apoint,r=8,fill="#f00")

fpoint = ppoint.polar(-73,opp)
p.add_dot(fpoint,r=8,fill="#0f0")

offset_contrux_line = D2line(fpoint,apoint)
p.add_line(offset_contrux_line,stroke="#0f0",stroke_width=2)

front_wheel_circle = D2circle(apoint,584/2-3)
p.add_circle(front_wheel_circle)

front_tire_circle = D2circle(apoint,584/2+19)
p.add_circle(front_tire_circle,stroke="#222",stroke_width=40)
front_sidewall_circle = D2circle(apoint,584/2+10)
p.add_circle(front_sidewall_circle,stroke="#5f4433",stroke_width=20)

curve_point = fpoint.polar(107,200)
control_point = fpoint.polar(107,50)
p.add_quad_bezier(curve_point,control_point,apoint,stroke="#fff",stroke_width=24)

p.saveas("bike.svg")

