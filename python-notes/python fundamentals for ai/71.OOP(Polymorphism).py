#Polymorphism

'''Polymorphism means that the same method name or function can produce different behaviours depending on the object it works with.
'''

#code

class Dog:
	def speak(self):
	   print("Woof!")

class Cat:
	def speak(self):
		print("Meow!")	
		
dog=Dog()
dog.speak() #Woof!

cat=Cat()
cat.speak() #Meow!		    