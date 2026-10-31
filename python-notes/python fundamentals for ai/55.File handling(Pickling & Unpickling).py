#Pickling & unpickling
'''
Pickling is a process of converting a python object into a binary format,& Unpickling is the inverse operation.it converts binary format into python object.'''

#pickling
def greet():
	return "hello how are you?"
a=greet()
#a is the function object	
import pickle
#we have to import pickle package for this.
with open("sample.pkl","wb") as f:
	pickle.dump(a,f)
#the file name will must in. pkl format.& we create the file in binary format.
#pickle.dump()-->converts function object(a) to binary format & transfers it into file object(f)

#unpickling
import pickle
with open("sample.pkl","rb") as f:
	P=pickle.load(f)
#pickle.load()-->converts binary data from file object to python object.	
	print(P) #hello how are you?		