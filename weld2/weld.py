from math import cos, sin, tan, sqrt, radians
sm_radius = 18			
lg_radius = 20
ang = radians(17.0) # inclination from 90 deg
for degs in range(180):
	rads = radians(degs*2)

	ty = round(sin(rads) * sm_radius, 3)
	tz = round(sqrt(abs(lg_radius**2 - ty**2)), 3)
	tx = round((cos(rads) * sm_radius / cos(ang)) + (tan(ang) * tz), 3)

	bead = 1.6 
	
	# POVRay spheres
	print('sphere { <' +str(tx) + ',' + str(ty) + ',' + str(tz) + '> ' + str(bead) + ' pigment { color rgb <1, 0, 0> } }')

	#OpenSCAD spheres
	#print(f"translate([{tx}, {ty}, {tz}]) sphere(r={bead}, $fn=12);")
