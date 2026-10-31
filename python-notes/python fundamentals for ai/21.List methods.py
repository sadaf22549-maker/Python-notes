#List methods
'''for adding elements-
.append(),.insert(),.extend()'''

L1=[1,2]
L2=[3,4]

L1.append(10) #it appends 10 at the last
print(L1) #[1,2,10]

L1.extend(L2) #it merges both list
print(L1) #[1,2,10,3,4]

L1.insert(0,100) #it adds an element(100) at 0th index
print(L1) #[100,1,2,10,3,4]

'''for removing elements-
.remove(),.pop(),.clear()'''

L=[2,6,5,8,9]
L.remove(6) #it removes 6 from the list

L.pop() #it removes the last element from the list
print(L) #[2,5,8]

L.clear()
print(L) #[ ]

'''for sorting & reversing elements-
.sort(),.sort(reverse=True),.reverse()'''

L=[2,6,0,1,8,5,9]
L.sort() #sorting in Ascending order
print(L) #[0,1,2,5,6,8,9]

L.sort(reverse=True) #sorting in Descending order
print(L) #[9,8,6,5,2,1,0]

L=[2,6,0,1,8,5,9]
L.reverse() #reversing
print(L) #[9,5,8,1,0,6,2]

'''others
.copy(),.index(),.count()'''

L_new=L.copy()
print(L_new) #[9,5,8,1,0,6,2]

print(L_new.index(8)) #2

print(L_new.count(5)) #1
#.count() returns the occurances of specific element