"""
Python: Binary Max Heap
"""
from math import inf


class BinaryMaxHeap:
    
    def __init__(self, capacity):
        self.heap_list = []
        self.current_size = 0
        self.cap = capacity
        
    def parent(self, i):
        return (i - 1) // 2
    
    def get_max(self):
        return self.heap_list[0]
    
    def heapify(self, i):
        l, r, largest = (2 * i) + 1, (2 * i) + 2, i
        
        if l < self.current_size and self.heap_list[l] > self.heap_list[largest]:
            largest = l
            
        if r < self.current_size and self.heap_list[r] > self.heap_list[largest]:
            largest = r
            
        if largest != i:
            self.heap_list[i], self.heap_list[largest] = \
                self.heap_list[largest], self.heap_list[i]
            
            self.heapify(largest)
            
    def extract_max(self, index=0):
        
        if self.current_size == 1:
            self.current_size -= 1
            data = self.heap_list[0]
            self.heap_list.remove(data)
            return data
            
        elif self.current_size > 1:
            self.current_size -= 1
            root = self.heap_list[index]
            i = index
            self.heap_list[index] = self.heap_list[-1]
            del self.heap_list[-1]
            self.heapify(i)
            return root
        
        return inf
    
    def delete_element(self, data):
        
        if self.current_size > 0:
            try:
                index = self.heap_list.index(data)
            except ValueError:
                return
            
            self.heap_list[index] = inf
            self.current_size -= 1
            i = self.current_size - 1
            
            while i != 0 and self.heap_list[self.parent(i)] < self.heap_list[i]:
                self.heap_list[i], self.heap_list[self.parent(i)] = \
                    self.heap_list[self.parent(i)], self.heap_list[i]
            
                i = self.parent(i)
            
            self.extract_max(index)
    
    def insert_element(self, data):
        
        if self.current_size == self.cap:
            return
        
        self.current_size += 1
        i = self.current_size - 1
        self.heap_list.append(data)
        
        while i != 0 and self.heap_list[self.parent(i)] < self.heap_list[i]:
            self.heap_list[i], self.heap_list[self.parent(i)] = \
            self.heap_list[self.parent(i)], self.heap_list[i]
            
            i = self.parent(i)
    
    def __str__(self):
        return ' '.join(list(str(i) for i in self.heap_list))
    

if __name__ == '__main__':
    cap, arr = 10, [9, 5, 1, 4, 2, 8, 3]
    heap = BinaryMaxHeap(cap)
    for i in arr:
        heap.insert_element(i)
        print("Heap {0}".format(heap))
    
    print("Before adding elements 6 & 7: [{0}]".format(heap))
    heap.insert_element(6)
    heap.insert_element(7)
    print("After adding elements 6 & 7: [{0}]".format(heap))
    print("Max Element: {0}".format(heap.get_max()))
    
    heap.delete_element(8)
    print("After deleting 8, the list [{0}]".format(heap))
    print("After extracting max {0}".format(heap.extract_max()))
    print("Heap After extracting max [{0}]".format(heap))
