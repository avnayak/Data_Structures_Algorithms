def reverseString(A):
	s,e=0,len(A)-1
	c=list(A)
	while s<=e :
		c[s],c[e]= c[e],c[s]
		s+=1
		e-=1
	return "".join(c)

print reverseString("Hello AKu")
