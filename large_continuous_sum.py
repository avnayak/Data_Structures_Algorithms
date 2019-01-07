'''
Given an array of integers (positive and negative) find the largest continuous sum.
'''
def large_continuous_sum(arr):
	arr1=[]
	arr2=[]
	maxm=[]
	if len(arr)==0:
		print "Its an empty array"
	for i in range(len(arr)):
		
		arr2=arr1
		arr2.append(arr[i])
		if sum(arr2)==0 or sum(arr2)<0:
			del arr1 [:]
			del arr2 [:]
		
		x=max(sum(arr1),sum(arr2))
		maxm.append(x)
	maxm.sort()
	y=maxm.pop()
	print "The large continuous sum is "
	print y
arr=[-1,1,-1,1,4,-2,9,-19,9]
large_continuous_sum(arr)
