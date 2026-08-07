from ADT import Node

class UnorderedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head 
        self.head = temp
        self.size = self.size + 1

    def search(self,item):
        current = self.head
        while (current != None):
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        prev = None
        if current == None:
            raise ValueError("Item not present in the list")

        if current.data == item:
            self.head = self.head.next
            self.size = self.size - 1
            return 

        while current is not None and current.data != item:
            prev = current
            current = current.next

        if current == None:
            raise ValueError("Item not present in the list")
        prev.next = current.next
        self.size = self.size - 1

    def __str__(self):
        current = self.head
        nodelist = []
        nodelist.append('[')
        while current != None:
            nodelist.append(str(current.data))
            if current.next != None:
                nodelist.append(',')
            current = current.next
        nodelist.append(']')
        return "".join(nodelist)

    def append(self,item):
        entry = Node(item)
        current = self.head
        self.size = self.size + 1
        if current == None:
            self.head = entry
            return 
        while current.next != None:
            current = current.next
        current.next = entry

    def index(self, item):
        counter = []
        count = 0
        current = self.head
        while current != None:
            if current.data == item:
                counter.append(count)
            current = current.next
            count = count + 1
        return counter

    def pop(self):
        current = self.head 
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None
        return current.data

    def insert(self, index, data):
        count = 0
        if index > self.size:
            raise ValueError("index out of bounds")
        current = self.head
        prev = None
        while count != index:
            prev = current
            current = current.next
            count = count + 1
        #we need to put item between prev and current
        item = Node(data)
        if index == 0:
            item.next = current
            self.head = item
        else:
            item.next = current
            prev.next = item
        self.size = self.size + 1

    def slice(self, start, stop):
        current = self.head
        count = 0
        if start > self.size or stop > self.size:
            raise ValueError("index out of bounds")
        while count != start:
            count = count + 1
            current = current.next
        slicestart = UnorderedList()
        while count < stop:
            slicestart.append(current.data)
            count = count + 1
            current = current.next
        return slicestart 

s = UnorderedList()
s.append(0)
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(4)
print(s)
print(s.slice(2,7))

