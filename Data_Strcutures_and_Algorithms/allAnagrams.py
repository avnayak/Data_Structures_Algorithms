def allAnagrams(s,p):
    result=[]
    for i in range(len(s)-1):
            if sorted(s[i:i+(len(p))]) == sorted(p):
                result.append(i)
    return result
    
    
 
s = "abab"
p = "ab"   
print allAnagrams(s,p)