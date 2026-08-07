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

def build_tree():
    atree = BinaryTree("a")
    atree.insert_left("b")
    atree.get_left_child().insert_right("d")
    atree.insert_right("c")
    atree.get_right_child().insert_left("e")
    atree.get_right_child().insert_right("f")
    return atree

