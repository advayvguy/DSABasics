class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self,root):
        if root is None:
            return 0
        return root.height
    
    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def rotateRight(self, root):
        l = root.left
        w = l.right

        root.left = w
        l.right = root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        l.height = 1 + max(self.getHeight(l.left), self.getHeight(l.right))

        return l
    
    def rotateLeft(self, root):
        r = root.right
        w = r.left

        root.right = w
        r.left = root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        r.height = 1 + max(self.getHeight(r.left), self.getHeight(r.right))

        return r 
    
    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif root.key > key:
            root.left = self.insert(root.left, key)
        elif root.key < key:
            root.right = self.insert(root.right, key)
        else:
            return root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            root = self.rotateRight(root)
        elif balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            root = self.rotateRight(root)
        elif balance < -1 and self.getBalance(root.right) <= 0:
            root = self.rotateLeft(root)
        elif balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            root = self.rotateLeft(root)
        
        return root
    
    def findsuccessor(self, root):
        succ = root.right
        while succ.left is not None:
            succ = succ.left
        return succ
    
    def delete(self, root, key):
        if root is None:
            return None
        elif root.key > key:
            root.left = self.delete(root.left, key)
        elif root.key < key:
            root.right = self.delete(root.right, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            succ = self.findsuccessor(root)
            root.key = succ.key
            root.right = self.delete(root.right, succ.key)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            root = self.rotateRight(root)
        elif balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            root = self.rotateRight(root)
        elif balance < -1 and self.getBalance(root.right) <= 0:
            root = self.rotateLeft(root)
        elif balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            root = self.rotateLeft(root)
        
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