#Recursion
'''Function calling itself repeatedly'''

def fibo(n):
 """this function takes integer as an input which   represents the nth term of fibonacci series"""
 if(n==0):
      return 0
 if(n==1):
      return 1

 return fibo(n-1) + fibo(n-2)

result = fibo(5)
print(result)