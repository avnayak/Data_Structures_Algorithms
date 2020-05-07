def twoSum(A,target):
    d = dict()
    ans= []
    for i in range(0,len(A)):
        search = target -A[i]
        if search in d:
            ans.append(d[search])
            ans.append(i)
        else :
            d[A[i]]=i
    return ans
    
    
    
A= [5,7,0,9,1,8]
target =13
print twoSum(A,target)
    