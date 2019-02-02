"""
An sequential search  problem
"""

choice=input("Enter the choice you want to select for the type of sequential search you want to perform\n")
if choice ==1:
	def sequential_search(array,element):
		pos=0
		found =False
		while pos<len(array) and  not found :
			if array[pos]==element:
				found=True
			else:
				pos  +=1
		return found
	array=[1,9,4,76,4]
	found=sequential_search(array,6)
	if found is True:
		print " The element found in the array is True"
	else:
		print "The element found in the array is False "
elif choice == 2:
	def sequential_search(array,element):
		pos=0
		found =False
		searched =False
		while pos<len(array) and  not found and  not searched :
			if array[pos]==element:
				found=True
			else:
				if array[pos]>element:
					searched	=True	
				else:	
					pos  +=1
		return found
	array=[22,45,67,100,709]
	found=sequential_search(array,00)
	if found is True:
		print " The element found in the array is True"
	else:
		print "The element found in the array is False "




























