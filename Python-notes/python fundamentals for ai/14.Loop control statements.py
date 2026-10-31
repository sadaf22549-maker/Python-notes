'''Loop control statement
1.Break-it will break the loop
2.continue-it will skip the current iteration
3.pass-it will basically used for running a loop without performing any actions.'''

list=['a','b','c','d','e']
for item in list:
	if(item=='c'):
	 break
	print(item,end=" ") 
print("\n")

for item in list:
	if(item=='c'):
		continue
	print(item,end=" ")		

for i in range(1,11):
				pass
				
				