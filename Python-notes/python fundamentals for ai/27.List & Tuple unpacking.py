#List & Tuple unpacking

a,b,c=[2,7,9]
print(a,b,c) #2 7 9
a,*others=[2,7,9]
print(a) #2
print(others) #[7,9]
'''here * basically used for containing other elements in others variable'''

a,b,c=(1,5,0)
print(a,b,c) #1 5 0