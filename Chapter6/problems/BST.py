class Node:
    def __init__(self, key):
        self.key = key 
        self.right = None
        self.left = None

class BinarySearchTree:

    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif root.key > key:
            root.left = self.insert(root.left, key)
        elif root.key < key:
            root.right = self.insert(root.right, key)
        return root 
    
    def findsuccessor(self, root):
        succ = root.right
        while succ.left is not None:
            succ = succ.left
        return succ
        
    def delete(self, root, key):
        #0 or 1 case
        if root is None:
            return None
        if root.key > key:
            root.left = self.delete(root.left, key)
        elif root.key < key:
            root.right = self.delete(root.right, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                succ = self.findsuccessor(root)
                root.key = succ.key
                root.right = self.delete(root.right, succ.key)
        return root
    
    def exists(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif root.key > key:
            return self.exists(root.left, key)
        else:
            return self.exists(root.right, key)