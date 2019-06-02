def climbing_stairs(n):
        a = b = 1
        for i in range(n-1):
            a, b = a + b, a

        return a
'''for i in range(2,n+2):
        ways[i]=ways[i-2]+ways[i-1]
    n=n+2
    return ways[n]
'''

print climbing_stairs(4)

