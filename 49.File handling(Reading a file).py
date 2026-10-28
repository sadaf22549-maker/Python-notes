#reading a file
#.read() reads the entire file

f=open("sample.txt","r")
#for reading we have to choose r mode.
data=f.read()
print(data)
file.close()