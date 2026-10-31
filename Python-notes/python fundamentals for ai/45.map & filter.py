#map,filter
'''map() is used for mapping items whereas filter() is used for filtering specific items.
syntax:
 map(lambda function,iterable data type)
 filter(lambda function,iterable data type)
 both of them returns object thats why we have to convert them into a list or any other data type.
 '''
L=[1,2,3,4,5]
a=list(map(lambda x:x**2,L))
print(a) #[1,4,9,16,25] 

a=list(filter(lambda x:x>3,L))
print(a) #[4,5]
 