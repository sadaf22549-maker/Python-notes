#while loop
'''while(condition):
	statement'''
#We have to stop this loop otherwise it will become an infinite loop

i=1
while(i<11):
	print(i)
	i+=1
	
#for loop
'''for iterator in string/list/tuple/dictionary/set/range:
	statement'''
#for loop is used for sequential traversing

list=[1,2,3,4,5]
for item in list:
	print(item)
for char in "hello":
	print(char)															#range(start,end) but remember end is excluded
#range() function is used for numericals 

for i in range(1,11):
	print(i)																														