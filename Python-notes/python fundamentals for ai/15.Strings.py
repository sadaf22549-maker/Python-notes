#string
str1="hello"
str2='''hello i am
       learning python''' #multiline-string
       
print(str1[0]) #we can address the characters of string by Indexing.variable_name[index]

#slicing

'''variable_name[starting_index:ending_index:steps] 
it is used for getting the specific part of a string.
By default the st_idx is 0,end_idx is len(string),& step is 1.
end_idx is excluded.
'''

print(str1[1:4]) #ell

#negative indexing
'''negative indexing is also possible in string for slicing.'''

sen="world" #here the idx of d is -1,then l is -2,r is -3 & so on.

print(str1[::-1])#reversing a string
