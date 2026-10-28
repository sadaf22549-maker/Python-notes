#Dictionaey comprehension
'''Syntax:
	D={key:value loop condition} '''
	
D={"num1":1,"num2":2,"num3":3,"num4":4}
D_new={i:D[i]**2 for i in D if D[i]>1}
print(D_new) #{"num2":4,"num3":9,"num4":16}	