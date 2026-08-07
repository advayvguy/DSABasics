from ADT import Node, UnorderedList

class Stack:
    def __init__(self):
        self.bucket = UnorderedList()

    def is_empty(self):
        if self.bucket.head == None:
            return True
        else:
            return False

    def push(self, data):
        item = Node(data)
        item.next = self.bucket.head
        self.bucket.head = item

    def pop(self):
        item = self.bucket.head.data
        self.bucket.head = self.bucket.head.next
        return item

    def peek(self):
        return self.bucket.head.data

    def size(self):
        current = self.bucket.head
        size = 0
        while current != None:
            current = current.next
            size = size + 1
        return size

    def __str__(self):
        current = self.bucket.head
        stacklist = []
        stacklist.append('[')
        while current != None:
            stacklist.append(str(current.data))
            if current.next != None:
                stacklist.append(',')
            current = current.next
        stacklist.append(']')
        return "".join(stacklist)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
print(s.peek())
print(s.pop())
print(s)
