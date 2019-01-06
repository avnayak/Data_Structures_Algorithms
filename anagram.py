#!usr/bin/python
import string
b="hello aku" 
c="aellOHUk"
b.lower()
print b
c.lower()
print c
b=b.split()
c=c.split()
b.sort()
c.sort()
print c 
if c==b:
	print "its an anagram"
