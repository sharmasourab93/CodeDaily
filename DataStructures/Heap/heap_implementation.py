"""
Python: Binary Heap Implementation
"""


class BinHeap:
    def __init__(self):
        self.heap_list = []
        self.current_size = 0

    def heapify_add(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = \
                    self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.heapify_add(self.current_size)

    def heapify_down(self, i):
        while i * 2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = \
                    self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2

        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        return_val = self.heap_list[0]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.heapify_down(1)

        return return_val

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = alist[:]

        while i > 0:
            self.heapify_down(i)
            i = i - 1


if __name__ == "__main__":
    heap = BinHeap()
    heap.build_heap([9, 5, 6, 2, 3])
    print(heap.del_min())
    print(heap.del_min())
    print(heap.del_min())
    print(heap.del_min())