def bubbleSort(arr):
    flag =0
    for count in range(1,len(arr)-1):
        for j in range(0,len(arr)-2):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=1
            if flag ==0:
                break
    return arr
            
    
    
arr=[1,4,5,6,7,8]    
print bubbleSort(arr)
    
    
    
    