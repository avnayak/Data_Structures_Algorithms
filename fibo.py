#!usr/bin/python

#Write a Python program to get the Fibonacci series

fibo=input("Enter the number of integers to implement fibonacci series \n")
print 1
fib=[]
for i in range(1,fibo):
	fib.append(i)
print fib
for i in range(0,fibo+1):
	if not(i==(fibo+1)):
		d=i+1
		c=fib[d]
		print fib[i]+c
	
