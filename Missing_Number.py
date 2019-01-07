def finder(arr1,arr2):
	count=[]
	arr1.sort()
	arr2.sort()	
	for i in range(len(arr1)):
		count.append(arr1[i])
	for i in range(len(arr2)):
		count.remove(arr2[i])
	print "The missing elements are \t"
	print count
arr1=[5,7,5,7]
arr2=[5,7]
finder(arr1,arr2)

