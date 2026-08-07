from node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while (current != None):
            count = count + 1
            current = current.next
        return count

    def search(self,item):
        current = self.head
        while(current != None):
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        return False

    def add(self,item):
        new_node = Node(item)
        if self.head == None or item < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return 

        current = self.head

        while current is not None and current.next.data <= item: #at current.next.data > item
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def print(self):
        current = self.head
        l = []
        while (current is not None):
            l.append(str(current.data))
            current = current.next
        return "".join(l)

mylist = OrderedList()

mylist.add(5)
mylist.add(2)
mylist.add(1)
mylist.add(4)
mylist.add(3)
print(mylist.print())
