class Heap:
    def __init__(self):
        self.list = []

    def peek(self):
        if len(self.list) == 0:
            return None
        return self.list[0]
    
    def insert(self, key):
        self.list.append(key)
        i = len(self.list) - 1
        while True:
            if i == 0:
                break
            parent_idx = (i-1)//2
            if self.list[i] > self.list[parent_idx]:
                self.list[i], self.list[parent_idx] = self.list[parent_idx], self.list[i]
                i = parent_idx
            else:
                break
    
    def _perc_down(self, i):
        while 2 * i + 1 < len(self.list):
            sm_child = self._get_max_child(i)
            if self.list[i] < self.list[sm_child]:
                self.list[i], self.list[sm_child] = (
                self.list[sm_child],
                self.list[i],
            )
            else:
                break
            i = sm_child

    def _get_max_child(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        if right >= len(self.list):
            return left

        if self.list[left] > self.list[right]:
            return left
        return right
    
    def delete(self):
        if len(self.list) == 0:
            raise KeyError("heap is empty")
        if len(self.list) == 1:
            return self.list.pop()
        self.list[-1], self.list[0] = self.list[0], self.list[-1]
        key = self.list.pop()
        self._perc_down(0)
        return key

    def heapify(self, nums):
        self.list = nums[:]
        i = len(self.list)//2 - 1
        while i >= 0:
            self._perc_down(i)
            i -= 1
    
    def size(self):
        return len(self.list)