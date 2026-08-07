from p35 import Node, DoublyList

class Spqueue:
    def __init__(self):
        self.line = DoublyList()

    def is_emptyi(self):
        if self.line.head == None:
            return True
        else:
            return False

    def enqueue(self, item): #O(1)
        self.line.add(item)

    def dequeue(self): #O(1)
        return self.line.flush()

    def size(self):
        return self.line.size

    def __str__(self):
        return self.line.__str__()

s = Spqueue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
print(s)
print(s.dequeue())
print(s)
