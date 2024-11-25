from math import cos, sin, tan, sqrt, radians
from random import randint
brad = 11.7
mrad = 13.3
ang = radians(0.0) # inclination from 90 deg
for degs in range(90):
	rads = radians(degs*4)

	tx = round(cos(rads) * brad,3)
	ty = round(sin(rads) * brad, 3)
	tz = round(sqrt(abs(mrad**2 - ty**2)), 3)

	#ty = round(sin(rads) * brad, 3)
	#tz = round(sqrt(abs(mrad**2 - ty**2)), 3)
	#tx = round((cos(rads) * brad / cos(ang)) + (tan(ang) * tz), 3)

	rr = 0.0 #randint(-5,5)/50.0

	bead = 2.5 + rr
	
	print('sphere { <' +str(tx) + ',' + str(ty) + ',' + str(tz) + '> ' + str(bead) + ' pigment {o} }')