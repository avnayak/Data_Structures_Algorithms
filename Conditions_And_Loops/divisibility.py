#!/usr/bin/python

n1=input("ENter the start of the range\n")
n2=input("ENter the end of the range\n")
c=[]
print "\n"
for i in range(n1,n2+1):
		if((i%7==0) and (i%5==0) and (i%10==0)):
			c.append(str(i))
print (','.join(c))

