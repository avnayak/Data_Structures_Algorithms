class insertionSort:
        def insertionSort(self):
            arr=[2,5,1,89,54,23,677,78]
            for i in range(1,len(arr)):
                 j=i-1 
                 while j>=0:
                    if arr[j]>arr[j+1]:
                            arr[j],arr[j+1]=arr[j+1],arr[j]
                    j-=1
            return arr
                    
x=insertionSort()
print x.insertionSort()

