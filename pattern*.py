#!usr/bin/python

for i in range(1,10):
	if i>(10/2):
		print str(*)*i
	else:
		for i in range((10/2),1,-1):
			print str(*)*i
	

