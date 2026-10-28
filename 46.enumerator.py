#enumerate
'''enumerate function is used basicalli in loops when we want the index no. with the specific items in a tuple format'''

L=["ahmed","Bappy","Sahil"]
for i in enumerate(L):
	print(i) #(0,ahmed)
	            #(1,Bappy)
	            #(2,Sahil)

'''enumerate has a parameter named start.by this,we can select the indexing which we want.By default the start's value is 0'''

for index,i in enumerate(L,start=1):
	print(index, i) #1 ahmed
	                       #2 Bappy
	                       #3 Sahil