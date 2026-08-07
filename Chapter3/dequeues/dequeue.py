class Dequeue:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return (not bool(len(self._items)))

    def add_rear(self,item):
        self._items.insert(0,item)

    def add_front(self,item):
        self._items.append(item)

    def size(self):
        return len(self._items)

    def remove_rear(self):
        return self._items.pop(0)

    def remove_front(self):
        return self._items.pop()
