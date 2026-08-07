from p10 import Heap

class PriorityQueue:
    def __init__(self):
        self.queue = Heap()
    
    def enqueue(self, key):
        self.queue.insert(key)
    
    def dequeue(self):
        return self.queue.delete()

    def peek(self):
        return self.queue.peek()
    
    def size(self):
        return self.queue.size()