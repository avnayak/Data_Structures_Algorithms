#leetcode 26
class Solution:
    def removeDuplicateFromSortedArray(self, nums):
         j=0
         for i in range(1,len(nums)):
                if nums[i]!=nums[j] :
                    j+=1
                    nums[j]=nums[i]
         return j+1
