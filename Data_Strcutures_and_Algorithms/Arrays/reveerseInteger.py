"""
Leetcode 7 Reverse INteger
"""
def reverse(a):
   res=0
   if a >= 0 :
        flag=True
   else:
        flag =False
        a=-a
   while a!=0:#We  have reversed the digit here
        if res >214748364:#to check for the overflow condition
            return 0
        else:
            res=res*10 + a%10
            a=a/10
   if flag is False:
        return -res
   else:
        return res

