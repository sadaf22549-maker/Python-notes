#Zip function
'''zip function combines 2,3 or multiple items in a tuple'''

L1=[1,2,3,4,5,6]
L2=[7,8,9,10,11,12]
zipper=list(zip(L1,L2)) #type-conversion is necessary,otherwise it returns zip object
print(zipper) #[(1,7),(2,8),(3,9),(4,10),(5,11),(6,12)]