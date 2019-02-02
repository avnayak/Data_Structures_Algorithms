#!/usr/bin/python

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

import random

try:
	n1=input("enter the number you want to guess \n")
	n2=input("enter the range of the random number \n")
	print "\n"
	i=random.randint(1,n2)
	print ("The actual random number is \n",i)
	if i<n1:
			print "guessed too high "
	elif i>n1:
			print "you guessed too low"
	else:
			print "You are correct"
except:
		print"Check whats the error"


