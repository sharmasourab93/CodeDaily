import sys

"""
#Single Iteration method
def print2largest(arr):
    if len(arr)<2:
        print(arr[1]," is the second largest element")
    first=-sys.maxsize-1
    second=-sys.maxsize-1

    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            second=arr[i]

    if second== -sys.maxsize-1:
        print("No second largest element found")
    else:
        print(second)
"""
#Using Heap method:
class Heap:
    def __init__(self,arr):
        self.arr=arr
        self.insertKey(self.arr)
    def left(self,i): return (2*i+1)
    def right(self,i): return (2*i+2)
    def parent(self,i): return (i-1)/2
    def heapify(self,i):
        smallest=i
        l=self.left(i)
        r=self.right(i)
        if self.arr[i]>self.arr[l]:
            smallest=l
        if self.arr[i]>self.arr[r]:
            smallest=r
        if smallest!=i:
            self.arr[i],self.arr[smallest]=self.arr[smallest],self.arr[i]
            self.heapify(smallest)
    def extractKey(self):
        if len(self.arr)==1: return self.arr[0]
        root=self.arr[len(self.arr)-1]
        self.arr[0]=self.arr[len(self.arr)-1]
        self.heapify(1)
        #return root
    def decreaseKey(self,i,new_val):
        self.arr[i]=new_val
        while i!=0 and self.arr[i]<self.arr[self.parent(i)]:
            self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
            i=self.parent(i)
    def deleteKey(self,i):
        self.decreaseKey(i,-sys.maxsize-1)
        self.extractKey()
    def findKthLargest(self,k):
        for i in range(k):
            self.deleteKey(0)
        return self.arr[0]

    def insertKey(self,*k):
        for i in range(len(k)):
            self.arr[i]=k[i]
            while i!=0 and self.arr[self.parent(i)]>self.arr[i]:
                self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
                i=self.parent(i)


#print2largest([1,2,3,4,5,7,23,6])
E=Heap([45,12,11,98,76,55,34,31])
x=E.findKthLargest(3)
print(x)