'''Leetcode 1
Two Sum
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)-1
        i,j=0,n
        
        while i<j:
            temp=nums[i]+nums[j]
            if temp==target:
                return i,j
            elif temp>target:
                    j-=1
            else :
                    i+=1
        return []
a=Solution()
print a.twoSum([2, 7, 11, 15],9)
            
        
            
