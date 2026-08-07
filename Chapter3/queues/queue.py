class Queue:

    def __init__(self):
        self._items = []

    def is_empty(self):
        if (len(self._items) == 0):
            return True
        else:
            return False

    def enqueue(self, item):
        self._items.insert(0,item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)


