#Set operations
#Union

S1={1,3,4,5}
S2={4,5,7,8}
print(S1|S2) #{1,3,4,5,7,8} 
# | is used for set union.

#Intersection

print(S1&S2) #{4,5}
# & is used for set intersection.

#difference

print(S1-S2) #{1,3}
# - is used for set difference

#symmetric difference

print(S1^S2) #{1,3,7,8}
# ^ is used for symmetric difference

#Loop operations
for item in S1:
	print(item,end=" ") #1 3 4 5

print("\n")

#membership operations
print(7 in S1) #False		