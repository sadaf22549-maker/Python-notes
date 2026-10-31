#Serialization & Deserialization
'''
Serialization-->it is a process of converting python data types to Json format.

Deserialization-->it is a process of converting Json to python data types.

.txt format has many limitations.for example it doesnt contain python data types.thats why we use json format.For this reason serialization & deserialization is important.'''

#serialization
import json
#we have to import json package for this.
D=[{"name":"Rakib","age":42,"Blood group":"B+"}]
with open("practice.txt","w") as f:
	json.dump(D,f,indent=4)
#json.dump() converts python data type(D) to json format & transfers it into file object(f).
#indent is a extra param for beautifying the output.	

#Deserialization
import json
with open("practice.txt","r") as f:
	P=json.load(f)
#json.load() converts the file object(f) containing json data to python data type.	
	print(P)
	