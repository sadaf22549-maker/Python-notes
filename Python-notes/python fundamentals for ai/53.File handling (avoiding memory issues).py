#avoiding memory issues
'''we can face memory issues if the. txt file is too big to open.in that case we have to read the file effectively.'''

#Chunking
'''we can avoid the memory issue by chunking.chunks are small parts of entire data containing specific characters.we can use the chunk_size as params of. read() to read the data effectively.After reading the certain chars,the buffer memory will remove it & make the space free
'''

with open("sample.txt","r") as f:
	chunk_size=10
	data=True
	while data:
		data=f.read(chunk_size)
		print(data,end="")