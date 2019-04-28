from itertools import permutations

def productExceptSelf(J):
    Res=[]
    if 1 in J:
        J.remove(1)
        perm=permutations(J)
        for i in list(perm): 
		print i
	     	g=reduce(lambda x, y: x * y, i)
             	Res.append(g)
	return Res
    
print productExceptSelf([1,2,3,4])
