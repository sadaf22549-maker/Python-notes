#Deal with multiple exceptions
try:
	with open("sample.txt","r") as f:
		data=f.read()
		print(data)
	a=5
	b=10
	print(a+m)
	L=[1,4,6,8,9]
	L[10]=50
	c=a/0
	print(c)
except FileNotFoundError:
	print("File not found")
#we have to mention specific exception name to deal with it.there are multiple exceptions like-zerodivisionerror,filenotfounderror,nameerror,keyerror etc.
except NameError:
	print("variable is not defined")
except IndexError:
	print("index not found")
except ZeroDivisionError:
	print("cant divide with 0")
except exception as e:
	print(e)
#this line executes when any unknown exception will happen.
finally:
	print("the program has finished")					