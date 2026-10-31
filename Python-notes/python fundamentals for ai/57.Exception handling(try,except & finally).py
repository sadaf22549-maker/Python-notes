#Errors
'''
There are 2 types of errors-
1)Compilation error(syntax error)
2)Run-time error-->exceptions
'''

#Exception handling
#try,except & finally
try:
	with open("sample3.txt","r") as f:
		data=f.read()
		print(data)
#try keyword tries to run this block of codes		
except:
	print("File not found")
#except keyword except the exception & runs the statement.
	
finally:
	print("The program has ended")	
#finally keyword always runs the statement whether there is exception or not.		