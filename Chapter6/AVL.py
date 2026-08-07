class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def height(self, N):
        if not N:
            return 0
        return N.height
    
    def getBalance(self, N):
        if not N:
            return 0
        return self.height(N.left) - self.height(N.right)
    
    def rightRotate(self, y):
        x = y.left 
        T2 = x.right # x < T2 < y

        #rotation-
        x.right = y
        y.left = T2

        #update heights
        y.height = 1 + max(self.height(y.right), self.height(y.left))
        x.height = 1 + max(self.height(x.right), self.height(x.left))

        #return root
        return x
    
    def leftRotate(self, y):
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        y.height = 1 + max(self.height(y.right), self.height(y.left))
        x.height = 1 + max(self.height(x.right), self.height(x.left))

        return x
    
    def insert(self, node, key):
        #perform BST insertion
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node
        
        #update height
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        #get balance
        balance = self.getBalance(node)

        #now there are 4 cases for rebalancing
        #case 1, if balance > 1 and key is less than the left node key value
        if balance > 1 and node.left.key > key:
            return self.rightRotate(node)

        #similarly for the left rotate case
        if balance < -1 and node.right.key < key:
            return self.leftRotate(node)

        #now for the case where balance > 1 but the key is greater than the key value of the left node
        if balance > 1 and node.left.key < key:
            node.left = self.leftRotate(node.left) #we left rotate node.left
            return self.rightRotate(node)
        
        if balance < -1 and node.right.key > key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        
        #if no changes:
        return node
    

    #for deletion too we do the standard BST deletion and put the balancing checks for each recursive call (or each level of the tree)

    def findsuccessor(self, node):
        succ = node.right
        while succ.left is not None:
            succ = succ.left
        return succ
    
    def delete(self, root, key):
        if not root:
            return None
        elif root.key > key:
            root.left = self.delete(root.left, key)
        elif root.key < key:
            root.right = self.delete(root.right, key)
        else:
            #0 or 1 children
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                #find successor:
                succ = self.findsuccessor(root)

                #copy the roots key with the successor:
                root.key = succ.key

                #delete the succ now
                root.right = self.delete(root.right, succ.key)
        
        if root is None:
            return root
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.getBalance(root)

                #now there are 4 cases for rebalancing
        #case 1, if balance > 1 and key is less than the left node key value
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        #similarly for the left rotate case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        #now for the case where balance > 1 but the key is greater than the key value of the left node
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left) #we left rotate node.left
            return self.rightRotate(root)
        
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        #if no changes:
        return root
    
    def display(self, root):
        """Prints an ASCII visual representation of the tree."""
        if not root:
            print("Tree is empty.")
            return

        lines, _, _, _ = self._display_aux(root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Helper method that recursively formats tree levels into string lines."""
        # Case 1: Leaf node
        if node.right is None and node.left is None:
            line = f"{node.key}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Case 2: Only left child
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = f"{node.key}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Case 3: Only right child
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = f"{node.key}"
            u = len(s)
            first_line = s + x * ' ' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Case 4: Two children
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = f"{node.key}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + s + y * ' ' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


avl = AVLTree()
root = None

for x in [30, 20, 40, 10, 25, 50]:
    root = avl.insert(root, x)

avl.display(root)
root = avl.delete(root, 25)
avl.display(root)
root = avl.delete(root, 50)
avl.display(root)
root = avl.delete(root, 40)
avl.display(root)