class Solution:
    def singleNumber(self, nums):
            num=[]
            nums.sort()
            for i in range(len(nums)+1):
                    print (nums[i])
                    if nums[i+1]==nums[i]:
                       num.append(nums[i])
                    
                    else:
                         pass
            return num
            
        
a=Solution()
a.singleNumber([4,1,2,1,2,6,6,6])
