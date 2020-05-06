def searchMatrix(A,target):
	m=len(A)
	n=len(A[0])
	i,j=0,n-1
	if  target <A[0][0]  and target> A[m-1][n-1]:
		return False
	while i<m-1  and j>=0:
		if target == A[i][j]:
			return i,j, True
		elif target < A[i][j]:
			j-=1
		else :
			i+=1
	return False
		
A=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
[10,11,12]
]

print searchMatrix(A,9)
