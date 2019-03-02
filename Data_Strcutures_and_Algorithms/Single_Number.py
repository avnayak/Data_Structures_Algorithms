from functools import reduce  
import operator
class Solution:
    def singleNumber(self, nums):

        
        return reduce(operator.xor, nums)
        
a=Solution()
a.singleNumber([4,1,2,1,2])
