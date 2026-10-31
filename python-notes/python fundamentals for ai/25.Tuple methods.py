#Tuple methods
'''.count(),.index()
.count() returns all the occurances of specific element
.index() returns the index of the 1st occurance of specific element'''

T=(2,4,2,4,6,8,0,4,3,1)
print(T.count(4)) #3
print(T.index(2)) #0

#Type-conversion
'''by converting tuple into list,we can use all the methods that can be used for a list'''

L=list(T)
L.append(50)
print(L)