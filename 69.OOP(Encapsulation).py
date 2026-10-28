#Encapsulation
'''encapsulation is used for saving internal data from being exposed.'''

#syntax:
#object_name.__param_name=value #private variable.
#object_name.param_name=value #public variable

#Code

class BankAccount:
	account_name="Sonali Bank Ltd."
	def __init__(self,name,balance):
		self.name=name
		self.__balance=balance #private variable
	
	def deposit(self,amount):
		if amount>0:
			self.__balance+=amount
		else:
			return "invalid"
	
	def withdraw(self,amount):
		if 0<amount<=self.__balance:
		  self.__balance-=amount
		else:
		  return "invalid"  	
		  
	def getbalance(self):
	   return self.__balance
	   
p1=BankAccount("Adil",10000)
p1.withdraw(5000)
print(f"bank account name:{p1.account_name}\nCurrent balance:{p1.getbalance()}")	   	  							  						
						
							