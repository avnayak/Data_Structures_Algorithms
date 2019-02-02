"""
A simple program of finding duplictes in an array using hashset to reduce the time complexity andin compare to brute force and sorting  and less space complexity in compare to hashmaps
"""
A = [1, 2, 3,1, 2, 3, 2, 3,1, 2, 3,3,234,3,12,3]
S = set()# A new set is created 
carry=0
y=input("Enter the number to be searched \n")
S.add(y)
for y in A:
 	if y in S :
		carry=carry+1
	else:
		pass
print "carry is " 
print carry

