#Inheritence

'''Inheritence is a property of OOP by which a class can inherit another class's attributes & methods.

parent class-->The class from which the                                        properties are taken.
Child class-->The class which consumes the                               properties.
'''

#code

class parent:
	def hello(self):
		print("hello from parent")

class child(parent): #Inherit
        pass
        
obj=child()
obj.hello() #hello from parent		