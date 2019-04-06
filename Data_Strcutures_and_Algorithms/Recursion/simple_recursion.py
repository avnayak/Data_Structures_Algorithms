#!usr/bin/python
def rt(num):
	if num<10:
		return num
	else:
		return (num%10)+rt(num/10)
x=rt(4322)
print x
