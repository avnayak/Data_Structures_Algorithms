''' Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)
'''
from itertools import permutations
def array_sum(arr,k):
	for i in range(len(arr)+1): 
		perm = permutations(arr,i+1)
		#print list(perm) 
		for i in list(perm):
	    		if sum(i)==k:
				print i
array_sum([1,3,4,0,2,2],4)
	 


