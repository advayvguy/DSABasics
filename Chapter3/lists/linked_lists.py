'''
    Node must contain the following information-
        data 
        and the next node
'''
from node import Node

class UnorderedList:

    def __init__(self):
        self.head = None
        self._last = None

    def is_empty(self):
        return self.head == None 

    def add(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        if (self._last == None):
            self._last = self.head

    def size(self):
        count = 0
        current = self.head
        while(current != None):
            count = count + 1
            current = current.next
        return count 

    def search(self,data):
        current = self.head
        while(current != None):
            if current.data == data:
                return True
            current = current.next
        return False

    def remove(self,data):
        current = self.head
        prev = None
        while current != None:
            if current.data == data:
                if prev == None:
                    self.head = current.next
                    if self.head == None:
                        self._last = None
                    return 
                else:
                    prev.next = current.next
                    if prev.next == None:
                        self._last = prev
                    return 
            prev = current
            current = current.next
        raise ValueError("element not in list")

    def append(self,item):
        if self._last == None:
            self.head = Node(item)
            self._last = self.head
        else:
            temp = Node(item)
            self._last.next = temp
            self._last = temp


mylist = UnorderedList()

mylist.append(1)
mylist.append(2)
print(mylist.size())
mylist.remove(1)
print(mylist.size())
mylist.append(3)
mylist.remove(3)
print(mylist.size())
