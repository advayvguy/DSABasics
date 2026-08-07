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

class Queue:

    def __init__(self):
        self._list = []

    def is_empty(self):
        return not bool(self._list)

    def size(self):
        return len(self._list)

    def enqueue(self, item):
        return self._list.insert(0,item)

    def dequeue(self):
        return self._list.pop()

    def peek(self):
        return self._list[-1]

class Deque:

    def __init__(self):
        self._list = []
    
    def is_empty(self):
        return not bool(self._list)

    def size(self):
        return len(self._list)
   
    def add_rear(self,item):
        self._list.insert(0,item)
    
    def add_front(self, item):
        self._list.append(item)

    def remove_rear(self):
        return self._list.pop(0)

    def remove_front(self):
        return self._list.pop()

class Node:

    def __init__(self, item):
        self._data = item
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self,item):
        self._data = item

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    next = property(get_next, set_next)


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head 
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while (current is not None):
            count = count + 1 
            current = current.next
        return count 

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
            return 

        while current is not None and current.data != item:
            prev = current
            current = current.next

        if current == None:
            raise ValueError("Item not present in the list")

        prev.next = current.next

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    
    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.left = self.left 
            self.left = new_node
    
    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.right = self.right
            self.right = new_node
    
    def get_root_val(self):
        return self.root
    
    def set_root_val(self, data):
        self.root = data

    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right