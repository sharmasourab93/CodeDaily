import time
def printarray(array,size):
    for i in range(size):
        print(array[i],end=" ")

def bubblesort(array,size):
    for i in range(size):
        for j in range(size-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    printarray(array,size)
    
def selectionsort(array,size):
    for i in range(size):
        min=i
        for j in range(size):
            if array[min]>array[j]:
                min=j
        array[i],array[min]=array[min],array[i]
    printarray(array,size)

def insertionsort(array,size):
    for i in range(1,size):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    printarray(array,size)

def main():
    array=[98,12,45,67,13,43,77]
    size=len(array)
    
    t1=time.time()
    bubblesort(array,size)
    t2=time.time()
    print("\nTime taken for Bubble Sort {0}".format(round(t2-t1,4)))
    
    t1=time.time()
    selectionsort(array,size)
    t2=time.time()
    print("\nTime taken for Selection Sort {0}".format(round(t2-t1,4)))

    t1=time.time()
    insertionsort(array,size)
    t2=time.time()
    print("\nTime taken for Insertion Sort {0}".format(round(t2-t1,4)))
    

main()
