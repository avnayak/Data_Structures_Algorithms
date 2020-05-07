'''Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28'''

def excelSheetColumn(A):
    ans =0
    pow =1
    for i in range(len(A)-1,0-1,-1):
        ans = ans + (ord(A[i])-64)*pow
        pow= pow*26
    return ans
    
print excelSheetColumn("AAA")
    
    