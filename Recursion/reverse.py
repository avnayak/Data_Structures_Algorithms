def reverse(s):
    
    # Base Case
    if len(s) <1:
        return s

    # Recursion
    
    return reverse(s[1:]) + s[0]
for i in range(1,len('abcsd')): 
	print reverse('abcsd')

