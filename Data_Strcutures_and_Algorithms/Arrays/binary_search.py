def binarySearch():
            arr=[2,5,1,89,54,23,677,78,90]
            arr.sort()
            print arr
            search_Key=5
            if search_Key<arr[(len(arr)/2)]:
                for i in range(len(arr)/2):
                    if search_Key==arr[i]:
                        return "Number found"
            elif search_Key>arr[(len(arr)/2)]:
                    for i in range((len(arr)/2+1),len(arr)):
                        if search_Key==arr[i]:
                            return "Number found"
            return "Number not found"
print binarySearch()
