'''
Leetcode 219
 Contains Duplicate II
'''
class Solution:
    def removeDuplicate(self, nums,k):
        for i  in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    if (j-i)<=k:
                        return True
        return False

