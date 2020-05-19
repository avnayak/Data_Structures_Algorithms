def searchRange(arr,target):
        ans=[]
        ans.append(firstOccurence(arr,target))
        ans.append(lastOccurence(arr,target))
        if ans[0] == -1 : #if element not found
            return -1
        else:
            return ans
def firstOccurence(arr,target):
        s,e=0,len(arr)-1
        first=-1
        while s<=e:
            mid=s+(e-s)/2
            if arr[mid] ==target:
                first=mid
                e=mid-1
            elif arr[mid] > target:
                e=mid-1
            else:
                s=mid+1
        return first
def lastOccurence(arr,target):
        s,e=0,len(arr)-1
        last=-1
        while s<=e:
            mid=s+(e-s)/2
            if arr[mid] ==target:
                last=mid
                s=mid+1
            elif arr[mid] > target:
                e=mid-1
            else:
                s=mid+1
        return last
    
target =3  
arr =[1, 2, 2, 2,2,4, 6, 7]
print searchRange(arr,target)