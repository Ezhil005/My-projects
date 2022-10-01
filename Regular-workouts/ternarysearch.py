def ternarysearch(arr,l,r,x):
    if l<=r:
        mid1=l+(r-l)//3
        mid2=mid1+(r-l)//3
        if arr[mid1]==x:
            return mid1
        elif arr[mid2]==x:
            return mid2
        elif arr[mid1]<x:
            return ternarysearch(arr,mid1+1,r,x)
        elif arr[mid2]>x:
            return ternarysearch(arr,l,mid2-1,x)
        return ternarysearch(arr,mid1-1,mid2+1,x)
    return -1
arr=[4,5,6,7,8,9,10,11,12]
x=10
print(ternarysearch(arr,1,len(arr),x))