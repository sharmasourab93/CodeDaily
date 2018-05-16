#Merge Sort
from math import floor as f
def merge(array,low,mid,high):

    n1=mid-low+1
    n2=high-mid

    L[n1]=None
    R[n2]=None

    for i in range(0,n1):
        L.append(array[low+i])
    for j in range(0,n2):
        R.append(array[mid+1+j])
    i=0
    j=0
    k=low

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            array[k]=L[i]
            i+=1
        else:
            array[k]=R[j]
            j+=1
        k+=1

        while i<n1:
            array[k]=L[i]
            i+=1
            k+=1
        while j<n2:
            array[k]=R[j]
            j+=1
            k+=1
        
def mergeSort(array,low,high):
    if low<high:
        mid=f(low+high)/2
        mergeSort(array,low,mid)
        mergeSort(array,mid+1,high)
        merge(array,low,mid,high)


array=[10,54,1,89,13,12,98]
mergeSort(array,0,len(array)-1)
print(array)
