class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def get_root(self):
        return self.root

    def set_root(self, node: Node):
        self.root = node
    
class Stack:

    def __init__(self):
        self._list = []

    def is_empty(self):
        return not bool(self._list)

    def size(self):
        return len(self._list)

    def peek(self):
        return self._list[-1]

    def push(self, item):
        self._list.append(item)

    def pop(self):
        return self._list.pop()
