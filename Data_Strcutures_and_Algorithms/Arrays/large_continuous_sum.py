'''
Given an array of integers (positive and negative) find the largest continuous sum.
'''
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
