#lambda function
'''lambda is a small anonymous function
syntax:
	lambda params:expression 
it returns an object.So,we have to store it in a variable.'''

print(lambda x,y:x+y) #object

a=lambda x,y:x+y
print(a(5,3)) #8

a=lambda x:'even' if x%2==0 else 'odd'
print(a(7)) #odd