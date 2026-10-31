#Functions

#Defining a function
'''syntax:
	def function_name(parameters):
		block of codes with return statement.

without return statement the function by default return the None value.Parameters are the containers which contain the values pass by the user.'''

def sum_of_two_numbers(a,b):
  sum=a+b
  return sum

#Calling a function
'''syntax:
  	function_name(arguements)    
arguements are the values pass by the user & parameters accept it.'''

result=sum_of_two_numbers(5,10)
print(result) #15	
  				
		