#Taking input in multiple objects

class students:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
list=[]		
for i in range(1,11):
	name=input(f"enter student{i} name:")
	marks=int(input(f"enter student{i} marks:"))
	student=students(name,marks)
	list.append(student)
for item in list:
	print(item.name, item.marks)			