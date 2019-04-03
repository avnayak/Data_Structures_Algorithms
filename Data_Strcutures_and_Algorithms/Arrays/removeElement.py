#leetcode 27
class Solution:
    def removeDuplicateFromSortedArray(self, nums,k):
         j=0
         for i in range(0,len(nums)):
                if nums[i]!=k :
                    nums[j]=nums[i]
                    j+=1
         print nums
                    
         return j
         
a=Solution()
print a.removeDuplicateFromSortedArray( [0,1,2,2,3,0,4,2],2)
