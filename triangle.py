#!usr/bin/python
from math import sqrt


def triangle_check(length2,length3,length1):

	if (length1>length2+length3) or (length2>length3+length1) or (length3>length2+length1):
		print "Its  a triangle"
	elif length1>length2 and length1>length3 and length1==sqrt(length2*length2+length3*length3):
		print "Its  a right-angled triangle"
	elif length2>length3 and length1==sqrt((length2*length2)-(length3*length3)):
			print "Its  a right-angled triangle"

	elif length3>length2 and length1==sqrt((length3*length3)-(length2*length2)):
				print "Its  a right-angled triangle"
	else:
		print "Its  not a triangle"
length1=input("Enter the 1st side \n")
length2=input("Enter the 2nd side \n")
length3=input("Enter the 3rd side \n")
triangle_check(length2,length3,length1)
