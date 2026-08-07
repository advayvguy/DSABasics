from ADT import Node, UnorderedList

class OrderedList(UnorderedList):
    
    def __init__(self):
        UnorderedList.__init__(self)

    def add(self, item):
        temp = Node(item)
        current = self.head
        prev = None
        if current == None or current.data > item:
            temp.next = current
            self.head = temp
            return 

        while current != None and current.data < item:
            prev = current
            current = current.next

        temp.next = current
        prev.next = temp 


    def search(self, item):
        current = self.head
        while current.data > item:
            current = current.next

        if current.data == item:
            return True 
        else:
            return False

    def remove(self, item):
        current = self.head
        prev = None

        if current == None:
            raise ValueError("Item not present in the list")

        if current.data == item:
            self.head = self.head.next
            return

        while current.data < item:
            prev = current
            current = current.next

        if current.data == item:
            prev.next = current.next
        else:
            return False

    def print(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

olist = OrderedList()
olist.add(4)
olist.add(3)
olist.add(2)
olist.add(1)
olist.add(2.5)
olist.add(0)
olist.remove(2.5)
olist.print()
