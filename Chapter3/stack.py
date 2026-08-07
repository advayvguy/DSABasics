class Stack:
    def __init__(self):
        self._items = [] #maybe we put the '_' before items to indicate that its private

    def is_empty(self):
        return not len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1] #i didnt know this was a thing?

    def size(self):
        return len(self._items)
