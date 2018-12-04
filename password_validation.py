# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password

#!/usr/bin/python
import re

def validate():
    while True:
        password = raw_input("Enter a password: ")
        if len(password) < 6 and len(password)>16:
            print("Make sure your password has minimum length 6 characters and maximum length 16 characters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
	elif re.search('[$#@]',password) is None: 
            print("Make sure your password has $#@ in it")
        else:
            print("Your password seems fine")
            break

validate()
