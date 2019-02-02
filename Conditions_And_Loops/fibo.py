#!usr/bin/python

#Write a Python program to get the Fibonacci series

n=input("Enter the number of integers to implement fibonacci series \n")

fib=[]
for i in range(1,n):
	fib.append(i) 
print " \n "
print fib 
print " \n "
print 1
for i in range(0,n):
		d=i+1
		if d<n-1:
			c=fib[d]
			print fib[i]+c
		else:
			break
