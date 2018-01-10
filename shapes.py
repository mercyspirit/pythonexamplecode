import math
class Line(object):
	
	def __init__(self, coor1, coor2):
		self.x1 = coor1[0]
		self.y1 = coor1[1]
		self.x2 = coor2[0]
		self.y2 = coor2[1]

	def distance(self):
		return math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2))
		

	def slope(self):
		return (self.y2 - self.y1)/(self.x2 - self.x1)

class Cylinder(object):
	pi = 3.14159
	def __init__(self, height = 1, radius = 1):
		self.height = height
		self.radius = radius
	def volume(self):
		return Cylinder.pi*(self.radius**2)*self.height
	def surface_area(self):
		return (2*Cylinder.pi*self.radius*self.height) + (2*Cylinder.pi*(self.radius**2))



#coordinates are tuples

l = Line((0,0),(1,1))
print(l.distance())
print(l.slope())

c = Cylinder(1,2)
print(c.volume())
print(c.surface_area())