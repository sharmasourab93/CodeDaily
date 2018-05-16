class MinHeap:
    def __init__(self):
        self.heap=[]
    def parent(self,i):return (i-1)/2
    def left(self,i):return (2*i+1)
    def right(self,i): return (2*i+2)

    def heapify(self,i):
        smallest=i
        l=left(i)
        r=right(i)
        if l<smallest and heap[l]<heap[]
