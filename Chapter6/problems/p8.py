#the heapify function is not optimal
class Heap:
    def __init__(self):
        self._list = []
    
    def peek(self):
        return self._list[0]
    
    def insert(self, key):
        self._list.append(key)
        i = len(self._list) - 1
        parent = (i-1)//2
        while i > 0:
            if self._list[i] < self._list[parent]:
                self._list[i], self._list[parent] = self._list[parent], self._list[i]
                i = parent
            else:
                break
            parent = (parent-1)//2
    
    def pop(self):
        if len(self._list) == 1:
            return self._list.pop()
        key = self._list[0]
        self._list[0] = self._list.pop()
        size = len(self._list)
        i = 0
        while True:
            left_index = 2*i + 1
            right_index = 2*i + 2
            if left_index >= size:
                break         
            elif right_index >= size:
                if self._list[i] <= self._list[left_index]:
                    break
                self._list[i], self._list[left_index] = self._list[left_index], self._list[i]
                break
            else:
                smallest = left_index
                if self._list[left_index] > self._list[right_index]:
                    smallest = right_index
                if self._list[i] <= self._list[smallest]:
                    break
                self._list[smallest], self._list[i] = self._list[i], self._list[smallest]
                i = smallest 
        return key
    
    def heapify(self, num_list):
        for i in num_list:
            self.insert(i)
    
    def print_heap(self):
        print(self._list)

def sort(nums):
    binheap = Heap()
    binheap.heapify(nums)
    for i in range(len(nums)):
        nums[i] = binheap.pop()

nums = [5,4,3,2,1,9]
sort(nums)
print(nums)