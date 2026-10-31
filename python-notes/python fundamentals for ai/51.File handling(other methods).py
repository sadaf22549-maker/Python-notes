#other methods of file handling

#.readline() -->reads the data line by line
f=open("sample.txt","r")
data1=f.readline()
data2=f.readline()
print(data1,data2)

#.tell()-->this gives us the position where the current cursor is pointing.
print(f.tell()) 

#seek(position) -->it shifts the cursor to the position which is given by us.
f.seek(0)
#moves the cursor to 0th position
data3=f.readline()
print(data3)

f.close()
