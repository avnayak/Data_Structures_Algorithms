# Write a Python program to check whether an alphabet is a vowel or consonant

#!usr/bin/python


p=raw_input("Enter a letter \n")
import re

if re.search('[aeiou]',p) is None:
			print "Its a alphabet"
else :
	print "Its a vowel"
