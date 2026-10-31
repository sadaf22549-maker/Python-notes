#Set methods
'''For adding elements-
.add(),.update()
.add() is used for adding only one element
.update() is used for adding multiple elements'''

S=set()
S.add(5)
print(S) #{5}
S.update([2,4,6])
print(S) #{2,4,6,5}

'''For removing element-
.remove(),.pop(),.clear()'''

S.remove(4)
print(S) #{2,6,5}
S.pop() #it removes a random element
print(S)
S.clear()
print(S) #set()

'''for copying-
.copy()'''

S1={2,7,8,0}
S2=S1.copy()
print(S2) #{2,7,8,0}

'''for set operations-
.union(),.intersection(),.isdisjoint(),.issubset()'''

S1={2,4,6,7,9,3}
S2={4,2,3,9}
print(S1.union(S2)) #{2,4,6,7,9,3}
print(S1.intersection(S2)) #{4,2,3,9}
print(S2.isdisjoint(S1)) #False
print(S2.issubset(S1)) #True