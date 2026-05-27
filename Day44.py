class Circle(): 
	def __init__(self):
		self.radius = int(input("ENTER RADIUS   "))

	def perimeter(self):
		self.perimeter= 2*3.14*self.radius
		return self.perimeter
		
	def area(self):
		self.area=3.14*self.radius*self.radius
		return self.area
		
p1=Circle()
print(p1.perimeter())
print(p1.area())