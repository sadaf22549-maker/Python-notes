#List comprehension
'''syntax:list=[expression loop condition]
it is used as a shortcut approach.'''

L=[5,8,4,2,1,9,6,3,4]
L_new=[item for item in L if item%2==0]
print(L_new) #[8,4,2,6,4]