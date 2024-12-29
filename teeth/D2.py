
import copy
from math import sin,cos,radians,sqrt,hypot,atan,degrees,atan2

def quadrant(obj,q):
	r = copy.copy(obj)
	if q in [2,3] :
		r.x = r.x * -1
	if q in [3,4] :
		r.y = r.y * -1
	return r

class D2(object):
	def __init__(self,x=0.0,y=0.0):
		self.x = float(x)
		self.y = float(y)
	#def __repr__(self):
	def tuple(self):
		return (float(self.x),float(self.y))
	def round2(self):
		r = copy.copy(self)
		r.x = round(float(self.x),2)
		r.y = round(float(self.y),2)
		return r
	def mirror_y(self):
		r = copy.copy(self)
		r.x = self.x * -1.0
		r.x = round(r.x,2)
		r.y = round(r.y,2)
		return r
	def mirror_x(self):
		r = copy.copy(self)
		r.y = self.y * -1.0
		r.x = round(r.x,2)
		r.y = round(r.y,2)
		return r
	def translate(self,x,y):
		r = copy.copy(self)
		r.x = self.x + float(x)
		r.y = self.y + float(y)
		r.x = round(r.x,2)
		r.y = round(r.y,2)
		return r
	def rotate(self,point,angle):
		r = copy.copy(self)
		angle_rad = radians(angle)
		r.x = point.x + cos(angle_rad) * (self.x - point.x) - sin(angle_rad) * (self.y - point.y)
		r.y = point.y + sin(angle_rad) * (self.x - point.x) + cos(angle_rad) * (self.y - point.y)
		r.x = round(r.x,2)
		r.y = round(r.y,2)
		return r
	def vector(self,distance,angle):
		r = copy.copy(self)
		r.x = cos(radians(angle)) * distance
		r.y = sin(radians(angle)) * distance
		r.x = r.x + self.x
		r.y = r.y + self.y
		r.x = round(r.x,2)
		r.y = round(r.y,2)
		return r
	def ho(self,h=None,o=None,quadrantrant=1): # y == o   x == a
		wh = float(h)
		wo = float(o)
		wa = sqrt(wh**2-wo**2)	
		tr = copy.copy(self)
		tr.x = wa
		tr.y = wo		
		return quadrant(tr,quadrantrant)
	def ha(self,h=None,a=None,quadrantrant=1): # y == o   x == a
		wh = float(h)
		wa = float(a)
		wo = sqrt(wh**2-wa**2)
		tr = copy.copy(self)
		tr.x = wa
		tr.y = wo		
		return quadrant(tr,quadrantrant)
	def ht(self,h=None,t=None,quadrantrant=1): # y == o   x == a
		wh = float(h)
		wt = float(t)
		wr = radians(wt)
		wa = wh * cos(wr)
		wo = wh * sin(wr)
		tr = copy.copy(self)
		tr.x = wa
		tr.y = wo		
		return quadrant(tr,quadrantrant)
	def rotzero(self, angle):
		new = D2()
		new.x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
		new.y = self.x * sin(radians(angle)) + self.y * cos(radians(angle))
		return new
	def mid(self,other): 
		r = copy.copy(self)
		r.x = (self.x + other.x) / 2
		r.y = (self.y + other.y) / 2
		return r
	def mid2(self,other,delta): 
		r = copy.copy(self)
		r.x = (self.x + other.x) / 2
		r.y = (self.y + other.y) / 2
		ang1 = degrees(atan2(float(r.y),float(r.x)))
		if ang1 < 0.0:
			ang2 = 360.0 + ang1
		else:
			ang2 = ang1
		len = sqrt(r.x**2 + r.y**2)
		len = len + delta
		f = D2().vector(len,ang2)
		return f
	def angle_and_length_to(self, other):
		dx = other.x - self.x
		dy = other.y - self.y
		length = hypot(dx, dy)
		angle = degrees(atan2(dy, dx))
		return angle, length


