#Tuple comprehension
'''Tuple comprehension is not available in python but we can emulate it.'''

T=(1,2,4,8,7,6,9,3)
T_new=tuple((item for item in T if item%2==0)) 
print(T_new) #(2,4,8,6)