class Employee:
	def __init__(self,role,department,salary):
		self.role=role
		self.department=department
		self.salary=salary
		

		
		
class Engineer(Employee):
		def __init__(self,name,age):
			self.name=name
			self.age=age
			super().__init__("engineer","cse","200000")
			
		def show_details(self):
			print(self.name)
			print(self.age)
			print(self.role)
			print(self.department)
			print(self.salary)
					
e1=Engineer("Het Modi","17")
e1.show_details()

