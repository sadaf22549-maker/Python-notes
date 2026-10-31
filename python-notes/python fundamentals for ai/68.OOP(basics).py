#Object Oriented Programming(OOP)
'''OOP organizes our data & makes it understandable!'''

class students: #class is used for creating blueprints

	school="abc pathshala" #Here school is class variable.class variable is common fol all objects
	
	def __init__(self,name,age,marks): #__init__ is used for initializing object with specific data.
#self -->current object

		self.name=name
		self.age=age
		self.marks=marks
#name,age,marks are instance variable.instance variable are unique per objects.

	def calculate_grade(self):
		if(self.marks>=80):
			return "A"
		else:
			return "B"
			
s1=students("Affan",24,68) #s1 is an object.object is an instance created by class.

print(s1.school) 
print(s1.name,s1.calculate_grade()) #here. name,.age,.calculate_grade() are the object methods.object methods are used for accessing specic info of an object.	
		