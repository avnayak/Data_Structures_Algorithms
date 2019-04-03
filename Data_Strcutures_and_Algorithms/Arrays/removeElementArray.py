''' #leetcode 27
    Remove  Element Array'''
class Solution:
    def removeDuplicate(self, nums,k):

        hash_set = []
	j=i+1
        for i in len(arr):
            for j in len(arr):
             	if i==j:
			if (j-i)<=k:
				return True
a=Solution()
print a.removeDuplicate([3,2,2,3],2)
