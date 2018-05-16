#Quick Sort

def swap(a,b):
    a,b=b,a
    return a,b

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

def partition(array,low,high):
    pivot=array[high]
    i=low-1

    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j]=swap(array[i],array[j])
    array[i+1],array[high]=swap(array[i+1],array[high])
    return (i+1)

array=[12,10,45,32,67,11,9]
quicksort(array,0,len(array)-1)
print(array)
