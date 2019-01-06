#!usr/bin/python
count =False
def is_Sublist(a,b):
	a.sort()
	b.sort()
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i]==b[j]:
				count=True
			else:
				count=False
	if count == True:
		print "Its a sublist"
	else:
		print "Its not a sublist"
a=[2,4,3,5,7]
b=[4,7,3,1]
is_Sublist(a,b)
