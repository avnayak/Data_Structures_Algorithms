def selectionSort(arr):
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            if arr[j] > arr[j+1]:
                    x=j+1
        if arr[i] > arr[x]:
            arr[i],arr[x]=arr[x],arr[i]
    return arr
            
    
    
arr=[7,5,8,1,6,9]    
print selectionSort(arr)
    
    
    
    