class bubbleSort:
        def bubbleSort(self):
            arr=[2,5,1,89,54,23,677,78]
            for i in range(len(arr)-1):#increases each time when the entire list is completed
                for j in range(len(arr)-i-1):#increases by moving right till it reaches end of the array
                    if arr[j]>arr[j+1]:
                            arr[j],arr[j+1]=arr[j+1],arr[j]
            return arr
                    
x=bubbleSort()
print x.bubbleSort()
            
                    
'''the rules you’re following:
1. Compare two numbers.
2. If the one on the left is taller, swap them.
3. Move one position right    '''
