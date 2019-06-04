def longestPalindromicSubstring(string):
    # Write your code here
    longest=""
    for i in range(len(string)):
        for j in range(i,len(string)):
            substring=string[i:j+1]
            if len(substring)>len(longest) and isPalindrome(substring):
                longest=substring
    return longest
                
def isPalindrome(substring):
    leftIndex=0
    rightIndex=len(substring)-1
    while leftIndex<rightIndex:
            if substring[leftIndex] != substring[rightIndex]:
                return False
            else:
                rightIndex-=1
                leftIndex+=1

    return True
string="abaxyzzyx"
print longestPalindromicSubstring(string)
