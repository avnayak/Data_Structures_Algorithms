"""
leetcode 69
"""
def mySqrt(x):
    if (x == 0 or x == 1): 
        return x 
    i = 0; result = 1
    while (result <= x): 
      
        i += 1
        result = i * i 
    return i-1
      
print mySqrt(25)
