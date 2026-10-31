#Abstraction

'''
Abstraction means hiding unnecessary implementation details & showing only the essential features to the user.
'''

#code

from abc import ABC,abstractmethod
#we import the required tools for abstraction

class Animal(ABC):
#By inheriting from ABC,we make Animal an abstract base class.

  @abstractmethod
  def sound(self):
  	pass
#This decorator marks sound() as an abstract method.Any child class must implement it before it's objects can be created.

class Dog(Animal):
	def sound(self):
	  print("bark....")
	  
dog=Dog()
dog.sound()	  		