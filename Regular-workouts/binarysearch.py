def binarysearch(arr,l,r,x):
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            r=mid-1
        elif arr[mid]<x:
            l=mid+1
        return -1
arr=[3,4,5,6,7,9,10]
x=6
print(binarysearch(arr,0,len(arr),x))
