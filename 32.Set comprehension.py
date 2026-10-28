#Set comprehension
'''syntax:
	S={expression loop condition}'''

S={2,3,1,4,7,9}
S_new={item for item in S if item%2==0} 
print(S_new) #{2,4}