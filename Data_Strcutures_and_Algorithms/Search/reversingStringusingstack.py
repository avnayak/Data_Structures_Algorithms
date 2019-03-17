'''
 Reversing a Word.
 A stack is used to reverse the letters. First the characters are extracted one by one from
the input string and pushed onto the stack. Then they’re popped off the stack and displayed.
Because of its last-in-first-out characteristic, the stack reverses the order of the
characters. 
'''
class stack(object):
    def __init__(self):
        l=raw_input()
        string=''
        c=l.split()
        for item in c[::-1]:
           string+=c.pop()
           string+="\t"
        print string
x=stack()

