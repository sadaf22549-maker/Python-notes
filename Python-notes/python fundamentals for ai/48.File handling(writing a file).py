#file handling
'''there are 2 types of files-text & binary
text-.txt,.csv,.log 
binary-.png,.jpg,.jpeg'''

#file I/O
'''it is done basically by 3 steps-
1.open a file
2.read/write data
3.close the file
'''
#open a file
'''syntax:
	open("path_of_existing_file","mode")
if the file is in same folder then we have to give only the file name otherwise we must give the full path for that file to open.

there are multiple modes available.we can choose in which mode we want to open our file'''

#modes
'''r-read mode.
 w-write mode.it overwrites.
 a-append mode.it adds the text at last of our file.
 rb-read binary data
 wb-write binary data
 r+ -read+write
 
note:in write or append mode,if the file doesnt exist,python will automatically creates that file in our internal storage.
'''
#open() function returns an object.so,we have to store it into a variable.

f=open("sample.txt","w")
#after creating the object we can use different methods like-.read(),.write(),.close()
#.write()-is used for writing

f.write("I am learning python\npython is a good language for learning Ai/ML\nI love programming in python!")
f.close()
#we must close our file after opening.
