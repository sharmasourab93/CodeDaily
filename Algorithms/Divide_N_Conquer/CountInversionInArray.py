#Count Inversion In Array
#Source: GeeksForGeeks
def merge(arr,temp,left,mid,right):
    i=0
    j=0
    k=0
    inv_count=0
    i=left
    j=mid
    k=left
    while i<=mid-1 and j<=right:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            i+=1
            k+=1
        else:
            temp[k]=arr[j]
            k+=1
            j+=1
            inv_count=inv_count+(mid-i)
    while i<=mid-1:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temp[k]=arr[j]
        j+=1
        k+=1
    for i in range(left,right):
        arr[i]=temp[i]
    return inv_count
def _mergeSort(arr,temp,left,right):
    inv_count=0
    if right>left:
        mid=(right+left)/2
        inv_count=_mergeSort(arr,temp,left,mid)
        inv_count+=_mergeSort(arr,temp,mid+1,right)
        inv_count+=merge(arr,temp,mid+1,right)
    return inv_count
#O(n log n) Solution
def mergesort(arr,arr_size):
    temp=[]*(arr_size-1)
    return _mergeSort(arr,temp,0,arr_size-1)

#O(n^2) Solutionn
def getInvCount(arr,n):
    inv_count=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                inv_count+=1
    return inv_count

arr=[1,20,6,4,5]
x=getInvCount(arr,len(arr))
y=mergesort(arr,len(arr)-1)
print(x)
