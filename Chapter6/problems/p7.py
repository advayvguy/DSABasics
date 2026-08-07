import operator

class BinaryTree:
    def __init__(self, key):
        self.key = key
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
        return self.key
    
    def set_root_val(self, data):
        self.key = data

    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left)
        preorder(tree.right)

def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.key)

def postordereval(tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    result1 = None
    result2 = None
    if tree:
        result1= postordereval(tree.left)
        result2= postordereval(tree.right)
        if result1 is not None and result2 is not None:
            return operators[tree.key](result1, result2)
        return int(tree.key)

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.key)
        inorder(tree.right)

def print_expr(tree):
    result = ""
    if tree:
        if tree.left is None and tree.right is None:
            result = result + str(tree.key)
        else:    
            result = "(" + print_expr(tree.left)
            result = result + str(tree.key)
            result = result + print_expr(tree.right) + ")"
    return result

def main():
    # Construct the expression tree for (3 + 4) * 5
    tree = BinaryTree("*")

    tree.insert_left("+")
    tree.insert_right("5")

    tree.get_left_child().insert_left("3")
    tree.get_left_child().insert_right("4")

    print("Preorder Traversal:")
    preorder(tree)

    print("\nInorder Traversal:")
    inorder(tree)

    print("\nPostorder Traversal:")
    postorder(tree)

    print("\nExpression:")
    print(print_expr(tree))

    print("\nEvaluated Result:")
    print(postordereval(tree))


if __name__ == "__main__":
    main()