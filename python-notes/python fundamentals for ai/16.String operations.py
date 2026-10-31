#string operations
#Arithmetic(+,*)
str1="hello"
str2="world"
print(str1+" "+str2) #hello world
'''its called concatination
for concatination we use this + symbol'''
print(str1*3) #hellohellohello
'''for repetetive string,we use this * symbol'''

#loops in string
for char in str1:
	print(char,end=" ")
print("\n")	
#membership operations
print('w' in str2) #True
print('o' not in str2) #False

#Relational operations
if(str1!=str2):
	print("its not equal")	