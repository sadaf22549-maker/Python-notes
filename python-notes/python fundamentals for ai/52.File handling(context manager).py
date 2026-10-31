#context manager
'''for opening file with the help of context manager,we have to use the with keyword.
context manager will automatically close the file after opening.so,we dont have to do this manually'''

#with keyword
with open("sample.txt","r") as f:
	data=f.read()
	print(data)