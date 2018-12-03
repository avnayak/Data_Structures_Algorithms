#!usr/bin/python

# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5 


q=raw_input("enter your string \n")
we=q.replace(" ","")
print q
count1=0
count2=0
count3=0
count5=0
count4=0
for i in q:
	if(i.isdigit())  :
		count1+=1
		if ((int(i)%2)==0):
			count2+=1
		else:count4+=1
			
	elif (i.isalpha()):
			count5+=1
	else:
		count3+=1
print ("EVEN NUMBERS",count2)
print ("ODD NUMBERS",count4)
print ("Digits",count1)
print ("other special characters",count3)
print ("Letters",count5)
