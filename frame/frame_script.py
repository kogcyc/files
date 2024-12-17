from d2stuff import *


svgStuff = ''

tiredia = 622+60
tirerad = tiredia/2
bbdrop = 80
bb = D2(-400,tirerad-bbdrop)
stlength = 510
ttlength = 550 + ((stlength - 550) / 2)
stext = 30
stt = bb.vector_to(stlength+stext,107)
stj = bb.vector_to(stlength,107)
htj = stj.vector_to(ttlength,0)

svgStuff = svgStuff + D2SVG_line(stj,htj) + '\n'
svgStuff = svgStuff + D2SVG_line(stt,bb) + '\n'

htc = htj.vector_to(500,-73)

line1 = D2Line().set_attr_two_points(htj,htc)                     # CONSTRUCTION LINE 1
#svgStuff = svgStuff + D2SVG_line(htj,htc) + '\n'


axle = D2(600,tirerad)
offset = axle.vector_to(68,197)
forkrace = offset.vector_to(356,107)
frc = forkrace.vector_to(450,180.01)                              # note: be sure to add .01 to angle to avoid division-BY-zero



line2 = D2Line().set_attr_two_points(forkrace,frc)                # CONSTRUCTION LINE 2
#svgStuff = svgStuff + D2SVG_line(forkrace,frc) + '\n'




intersection = line1.intersection_with(line2)
diff = abs(intersection.x - forkrace.x)

axle = D2(600-diff,tirerad)
offset = axle.vector_to(68,197)
forkrace = offset.vector_to(356,107)

svgStuff = svgStuff + D2SVG_line(axle,forkrace) + '\n'
svgStuff = svgStuff + D2SVG_line(axle,offset) + '\n'
svgStuff = D2SVG_circle(axle,tirerad) + '\n' + svgStuff 


copy_clipboard(svgStuff)

