#Lists

L=[1,3,5,"Abid",'B',2+3j,False] #its a list which can contain multiple data types.It is mutable & can contain duplicate values.

new_L=[ ] #empty list
new_L=[1,2,3] #1D list
new_L=[1,2,[3,4,5]] #2D list
new_L=[[[1,2],[3,4]],[[5,6],[7,8]]] #3D list

#Indexing & slicing
print(L[3]) #Abid
print(L[1:6]) #[3,5,Abid,B,(2+3j)]

L[6]=True
print(L) #[1,3,5,Abid,B,(2+3j),True]