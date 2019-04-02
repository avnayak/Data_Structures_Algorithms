''' #leetcode 27
    Remove  Element Array'''
class Solution:
    def removeDuplicate(self, nums,val):

        hash_set = []

        for num in nums:
            if num !=val :
                hash_set.append(num)

        return len(hash_set)

a=Solution()
print a.removeDuplicate([3,2,2,3],2)
