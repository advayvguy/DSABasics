class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    next = property(get_next, set_next)

    def get_prev(self):
        return self._prev

    def set_prev(self, prev):
        self._prev = prev

    prev = property(get_prev, set_prev)

    def __str__(self):
        return str(self._data)

class DoublyList:
    def __init__(self):
        self.head = None

    #we add the new element to the head
    #new head- prev = current head.prev next = current head
    #old head- prev = new head next- no change in the next

    def add(self, data):
        item = Node(data)
        if self.head == None:
            self.head = item
            self.head.next = self.head
            self.head.prev = self.head
        else:
            item.next = self.head
            item.prev = self.head.prev
            self.head.prev.next = item
            self.head.prev = item
            self.head = item

    def size(self):
        if self.head == None:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            current = current.next
            count = count + 1
        return count

    def search(self, item):
        current = self.head
        while current.next != self.head:
            if current.data == item:
                return True
            current = current.next
        if current.data == item:
            return True 
        return False

    def remove(self, item):
        current = self.head
        prev = current.prev
        if current.data == item:
            if prev == current:
                self.head = None
                return 
            current.prev.next = current.next
            current.next.prev = current.prev
            self.head = current.next
            return 
        current = current.next
        while current != self.head:
            if current.data == item:
                current.prev.next = current.next
                current.next.prev = current.prev
                return 
            prev = current
            current = current.next

        raise ValueError("item not present in the list")

    def __str__(self):
        current = self.head
        if current == None:
            return "[]"
        current = current.next
        outlist = ['[',str(self.head.data),',']
        while current != self.head:
            outlist.append(str(current.data))
            if current.next != self.head:
                outlist.append(',')
            current = current.next
        outlist.append(']')
        return "".join(outlist)

    def flush(self):
        target = self.head.prev
        topop = target.data
        if target == self.head:
            self.head = None
        else:
            self.head.prev = self.head.prev.prev
            target.prev.next = self.head
        return topop

