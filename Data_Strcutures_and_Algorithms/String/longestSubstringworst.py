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
    for i in range(len(substring)):
        for j in range(i+1,len(substring)):
            if substring[i]==substring[j]:
                return False
    return True
string="clementisacap"
print longestPalindromicSubstring(string)
