class Student():
	
	def __init__(self,name,marks1,marks2,marks3):
		self.name =name
		self.marks1=marks1
		self.marks2=marks2
		self.marks3=marks3
		
	def sum(self):
		self.sum = self.marks1+self.marks2+self.marks3
		print(self.sum)
		
	def avg(self):
		self.avg=self.sum/3
		print(self.avg)
		
s1=Student("Het",91,93,82)
print(s1.name)
s1.sum()
s1.avg()
		