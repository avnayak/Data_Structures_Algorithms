def countZeros(n):
    if n ==0:# base case
        return 0
    
    smallAns= countZeros(n/10) #Recursive case
    lastDigit = n%10
    if lastDigit ==0 :
         smallAns+=1
    else :
         smallAns
    
    return smallAns
        
    
    
    
    
    
print countZeros(70080)