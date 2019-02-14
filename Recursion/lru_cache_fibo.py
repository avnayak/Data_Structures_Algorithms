#!usr/bin/python
from functools import lru_cache
@Lru_cache(maximumsize=1000)
def fibo(n):
	if n<0 and type(n)!=int:
		raise TypeError("The number is not an integer and cant be in fibonacci series group please try again")
	if n in fibo_cache:
		return fibo_cache[n] #the n represents there are 'n' numbers ahead and we want to know the result of those 'n' numbers 
	elif n==0:
		return 0
	elif n==1:#checking the base condition
	 	return 1# if you find series starting like this 1,1,2
	elif n==2:
		return 1# if you find series starting like this 0,1,1,2
	else :
			return fibo(n-2)+ fibo(n-1)
#x=fibo(0)
#print x
for i in range(1,9):
	print fibo(i)
