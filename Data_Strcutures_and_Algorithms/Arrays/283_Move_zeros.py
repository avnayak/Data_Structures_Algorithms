def moveZeros(nums):
    for i in nums:
        if i==0:
            nums.remove(i)
            nums.append(0)
    return nums
    
    
    
    
print moveZeros([0,1,0,3,12])
