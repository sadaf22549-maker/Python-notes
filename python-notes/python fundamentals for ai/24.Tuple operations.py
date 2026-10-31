#Tuple operations
#Arithmetic operations(+,*)
T1=(1,2,3)
T2=(4,5,6)
print(T1+T2) #(1,2,3,4,5,6)
print(T1*2) #(1,2,3,1,2,3)

#Loop operations
for item in T1:
	print(item,end=" ")
print("\n")	

#membership operations
print(5 in T2)