def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetter=[]
    key=key%26#A key that lies in the range of 1 and 26
    for letter in string:
        newLetter.append(getCipher(letter,key))
    return "".join(newLetter)
        
        
def getCipher(letter,key):
            shift=ord(letter)+key
            return chr(shift) if shift<=122 else chr(96 + shift%122)
            
            
print caesarCipherEncryptor("xyz", 27)
