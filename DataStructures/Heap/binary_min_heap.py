"""
Python: Binary Min Heap
"""
from math import inf


class BinaryMinHeap:
    
    def __init__(self, capacity):
        self.heap_list = []
        self.current_size = 0
        self.cap = capacity
        
    # Returns the Parent node of the index
    def parent(self, i):
        return (i - 1) // 2
    
    def get_min(self):
        return self.heap_list[0]
    
    # Build Heap Property
    def heapify(self, i):
        l, r, smallest = (2 * i) + 1, (2 * i) + 2, i
        
        if l < self.current_size and self.heap_list[l] < self.heap_list[smallest]:
            smallest = l
            
        if r < self.current_size and self.heap_list[r] < self.heap_list[smallest]:
            smallest = r
        
        if smallest != i:
            self.heap_list[smallest], self.heap_list[i] = \
                self.heap_list[i], self.heap_list[smallest]
            
            self.heapify(smallest)
    
    # Extract Min
    def extract_min(self, index=0):
        
        if self.current_size == 1:
            self.current_size -= 1
            data = self.heap_list[0]
            self.heap_list.remove(data)
        
            return data
        
        elif self.current_size > 1:
            
            self.current_size -= 1
            root = self.heap_list[index]
            self.heap_list[index] = self.heap_list[self.current_size - 1]
            del self.heap_list[self.current_size - 1]
            self.heapify(index)
            
            return root
        
        return inf
        
    def insert_element(self, data):
        
        if self.current_size == self.cap:
            return
        
        self.current_size += 1
        i = self.current_size - 1
        self.heap_list.append(data)
        
        # Maintain Heap Property
        while i != 0 and self.heap_list[self.parent(i)] > self.heap_list[i]:
            self.heap_list[i], self.heap_list[self.parent(i)] = \
                self.heap_list[self.parent(i)], self.heap_list[i]
            i = self.parent(i)
    
    def delete_element(self, data):
        if self.current_size > 0:
            try:
                index = self.heap_list.index(data)
            except ValueError:
                return
            
            self.heap_list[index] = -inf
            self.current_size -= 1
            i = self.current_size
            
            # Maintaining Heap Property
            while i != 0 and self.heap_list[self.parent(i)] > self.heap_list[i]:
                self.heap_list[i], self.heap_list[self.parent(i)] = \
                    self.heap_list[self.parent(i)], self.heap_list[i]
                i = self.parent(i)
            
            self.extract_min(index)
        
    
    def __str__(self):
        return ' '.join(list(str(i) for i in self.heap_list))


if __name__ == '__main__':
    cap, arr = 5, [9, 5, 1, 4, 2, 8, 3]
    heap = BinaryMinHeap(cap)
    for i in arr:
        heap.insert_element(i)
        # print("Heap {0}".format(heap))
    
    print("Before adding elements 6 & 7: [{0}]".format(heap))
    heap.insert_element(6)
    heap.insert_element(7)
    print("After adding elements 6 & 7: [{0}]".format(heap))
    print("Minimum Element: {0}".format(heap.get_min()))
    
    heap.delete_element(8)
    print("After deleting 8, the list [{0}]".format(heap))
    
    print("Extract Min {0}".format(heap.extract_min()))
    print("Heap After extracting min {0}".format(heap))
    print("Get Min {0}".format(heap.get_min()))
    print(heap)
    
    print("\nExtract Min {0}".format(heap.extract_min()))
    print(heap)
