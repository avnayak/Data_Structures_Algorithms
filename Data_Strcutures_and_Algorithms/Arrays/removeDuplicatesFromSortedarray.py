''' #leetcode 26
    Remove Duplicates from Sorted Array'''
class Solution:
    def removeDuplicate(self, nums):

        hash_set = set()

        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
            hash_set.add(num)

        return len(hash_set)
        

