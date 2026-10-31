# *args & **kwargs
'''When the parameters or the arguements are not fixed,in that case we have to use *args or **kwargs.
*args-->creates a tuple
**kwargs-->creates a dictionary
'''

# *args
def demo1(*args):
 print(args) #(2,4,6,8)
 for i in args:
 	print(i,end=" ") #2 4 6 8
 
demo1(2,4,6,8) 
print("\n")

# **kwargs
def demo2(**kwargs):
	print(kwargs) #{"name":"Arif","mark":20,"grade":'C'}
	for i in kwargs:
		print(i, kwargs[i]) #name:Arif
		                              #mark:20
		                              #grade:C
	
demo2(name="Arif",mark=20,grade='C')	

'''in **kwargs we have to mention variable names assigning with values but not for *args '''