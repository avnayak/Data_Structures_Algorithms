'''
Given an array of integers (positive and negative) find the largest continuous sum.
'''
"""
whenever the sum goes to 0, change the sum to 0
else continue your sum 
and whatever the current sum is match with the new sum 
which ever is the maxm , add it
"""
def maximum(nums):
        ThisSum = 0
        MaxSum = -10000
        
        for i in range( 0, len(nums) ):
            if ThisSum < 0:
                ThisSum = 0
            ThisSum = ThisSum + nums[ i ]
            MaxSum = max( ThisSum, MaxSum )

        return MaxSum    
print maximum([-2,1,-3,4,-1,2,1,-5,4])
