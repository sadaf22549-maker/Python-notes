#Dictionary operations
#membership operations

D={"phone":"Realme","price":20000}
print("phone" in D) #True
#membership,loop operations work for keys,not for values.

#Loop operations
for item in D:
	print(item,end=" ") #phone price
print("\n")	
for item in D:
	print(item, D[item])  #phone realme              price 20000