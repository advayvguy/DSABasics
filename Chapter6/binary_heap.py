class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def get_min(self):
        return self.heap[0]
    
    def perc_up(self, i):
        while (i-1)//2 > 0:
            parent_id = (i-1)//2
            if self.help[parent_id] > self.heap[i]:
                self.heap[parent_id], self.heap[i] = self.heap[i], self.heap[parent_id]
            i = parent_id

    def insert(self, item):
        self.heap.append(item)
        self.perc_up(len(self.heap)-1)
        self.size += 1

    def get_min_child(self, i):
        if 2*i+2 > self.size - 1:
            return 2*i+1
        if self.heap[2*i+1] > self.heap[2*i+2]:
            return 2*i+1
        return 2*i+2
    
    def perc_down(self, i):
        while 2*i+1 < len(self.heap):
            sm_child = self.get_min_child(i)
            if self.heap[i] > self.heap[sm_child]:
                self.heap[i], self.heap[sm_child] = self.heap[sm_child], self.heap[i]
            else:
                break
            i = sm_child

    def delete(self):
        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        val = self.heap.pop()
        self.perc_down(0)
        return val
    
    def heapify(self, nums):
        self.heap = nums[:]
        i = len(self.heap)//2 - 1 #this is the last parent node
        while i >= 0:
            self.perc_down(i)
            i = i - 1