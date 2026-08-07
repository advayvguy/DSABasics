from ADT import Node, UnorderedList

class Queue:

    def __init__(self):
        self.line = UnorderedList()

    def is_empty(self):
        if self.line.head == None:
            return True 
        else:
            return False

    def enqueue(self, data):
        item = Node(data)
        current = self.line.head
        if current == None:
            self.line.head = item 
            return 
        while current.next != None:
            current = current.next

        current.next = item

    def dequeue(self):
        item = self.line.head
        if item == None:
            return 
        self.line.head = self.line.head.next
        return item.data

    def size(self):
        count = 0
        current = self.line.head
        while current != None:
            current = current.next
            count = count + 1
        return count 

    def __str__(self):
        current = self.line.head
        outlist = []
        outlist.append('[')
        while current != None:
            outlist.append(str(current.data))
            if current.next != None:
                outlist.append(',')
            current = current.next
        outlist.append(']')
        return "".join(outlist)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
q.dequeue()
print(q)
