from general_dfs import DFSGraph
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def shift_up(self, i):
        index = i
        while index > 0:
            parent_index = (index-1)//2
            if self.queue[index][0] < self.queue[parent_index][0]:
                self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]
            else:
                break
            index = parent_index
            
    def add(self, key):
        self.size += 1
        self.queue.append(key)
        index = self.size - 1
        self.shift_up(index)

    def shift_down(self, i):
        index = i
        while True:
            left_index = 2*index + 1
            right_index = 2*index + 2
            if left_index >= self.size:
                break

            smaller = left_index

            if right_index < self.size:
                if self.queue[right_index][0] < self.queue[left_index][0]:
                    smaller = right_index
            
            if self.queue[index][0] <= self.queue[smaller][0]:
                break 

            self.queue[smaller], self.queue[index] = self.queue[index], self.queue[smaller]
            index = smaller

    def pop(self):
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        key = self.queue.pop()
        self.size -= 1
        self.shift_down(0)
        return key 
    
    def heapify(self, arr):
        self.queue = arr
        self.size = len(arr)

        index = (self.size//2) - 1
        
        while index >= 0:
            self.shift_down(index)
            index -= 1
    
    def change_priority(self, new_distance, v):
        for i in range(self.size):
            if self.queue[i][1] == v:
                self.queue[i] = (new_distance, v)
                self.shift_up(i)
                break
    
    def __bool__(self):
        return self.size 
    
def dijekstra(graph, start):
    pq = PriorityQueue()
    start.distance = 0
    pq.heapify([(v.distance, v) for v in graph])
    while pq:
        distance, current_v = pq.pop()
        for next_v in current_v.get_neighbors():
            edge_weight = current_v.get_neighbor(next_v)
            new_distance = current_v.distance + edge_weight
            if new_distance < next_v.distance:
                next_v.distance = new_distance
                next_v.previous = current_v

                pq.change_priority(new_distance, next_v)