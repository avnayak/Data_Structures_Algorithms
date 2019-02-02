#!usr/bin/python


# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

q=raw_input("enter your string \n")
we=q.replace(" ","")
print q
count1=0
count2=0
count3=0
for i in q:
	if(i.isdigit())  :
		count1+=1
	elif (i.isalpha()):
			count2+=1
	else:
		count3+=1
print ("Letters",count2)
print ("Digits",count1)
print ("other special characters",count3)

