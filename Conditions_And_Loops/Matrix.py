#!usr/bin/python
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
rows=input("Enter  the number of rows\n");
columns=input("Enter  the number of columns\n");
Matrix=[[1 for col in range(columns)] for row in range(rows)]
print Matrix
for rows in range(rows):
	for columns in range(columns):
		c=(rows*columns)
		Matrix[rows][columns]=c

print Matrix
