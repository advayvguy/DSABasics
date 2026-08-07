#the class BST captures the whole tree in general
class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self, key, value):
        current_node = self.root
        if self.root == None:
            self.root = TreeNode(key, value)
            self.size += 1
            return 
        while True:
            if current_node.key == key:
                current_node.value = value 
                return 
            if current_node.key > key:
                if current_node.left is None:
                    current_node.left = TreeNode(key, value, parent = current_node)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = TreeNode(key, value, parent = current_node)
                    break
                else:
                    current_node = current_node.right 
        self.size += 1
    
    def _put(self, node, key, value):
        if node is None:
            self.size += 1
            return TreeNode(key, value)
        
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        
        return node 
    
    def putr(self, key, value):
        self.root = self._put(self.root, key, value)
    
    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            elif current_node.key > key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    
    def _get(self, node, key):
        if node == None:
            return False
        elif node.key == key:
            return node
        elif node.key > key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)
        
    def getr(self, key):
        if self.root:
            result = self._get(self.root, key)
            if result:
                return result.value
        return None
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        return self.get(key) is not False
    
    def findsuccessor(self, node):
        succ = node.right
        while succ.left is not None:
            succ = succ.left
        return succ

    def _delete(self, root, key):
        if root is None:
            return None
        
        if root.key > key:
            root.left = self._delete(root.left, key)
        elif root.key < key:
            root.right = self._delete(root.right, key)
        else:
            #0 or 1 children-
            if root.left is None:
                return root.right #returns a none in case of leaf and right in case of one child
            elif root.right is None:
                return root.left
            
            #case for 2 children

            #find successor
            succ = self.findsuccessor(root)
            
            #replace current node with the successor
            root.key, root.value = succ.key, succ.value

            #delete the successor
            root.right = self._delete(root.right, succ.key)
        return root
    
    def __delitem__(self, key):
        if key in self:
            self.size -= 1
        self.root = self._delete(self.root, key)

            
    
class TreeNode:
    def __init__(self, key, value, right = None, left = None, parent = None):
        self.key = key
        self.value = value 
        self.right = right
        self.left = left 
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left is self #the first condition to see if it its a root
    
    def is_right_child(self):
        return self.parent and self.parent.right is self 
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return self.right is None and self.left is None
    
    def has_any_child(self):
        return self.right or self.left
    
    def has_children(self):
        return self.right and self.left
    
    def replace_value(self, key, val, left, right):
        self.key = key 
        self.value = val
        self.left = left
        self.right = right 
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    #yield- unlike return it freezes the state of the program until another request or a call is made
    #we use an inorder to traverse through the tree
    def __iter__(self):
        if self:
            if self.left:
                for elem in self.left:
                    yield elem
            yield self.key
            if self.right:
                for elem in self.right:
                    yield elem

my_tree = BST()
my_tree["a"] = "a"
my_tree["q"] = "quick"
my_tree["b"] = "brown"
my_tree["f"] = "fox"
my_tree["j"] = "jumps"
my_tree["o"] = "over"
my_tree["t"] = "the"
my_tree["l"] = "lazy"
my_tree["d"] = "dog"

print(my_tree["q"])
print(my_tree["l"])
print("There are {} items in this tree".format(len(my_tree)))
del my_tree["a"]
print("There are {} items in this tree".format(len(my_tree)))

for node in my_tree:
    print(my_tree[node], end=" ")
print()