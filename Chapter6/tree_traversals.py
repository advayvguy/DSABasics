from ADT import BinaryTree
import operator

def preorder(tree):
    if tree:
        print(tree.root)
        preorder(tree.left)
        preorder(tree.right)

def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.root)

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
        if result1 and result2:
            return operator[tree.key](result1, result2)
        return tree.key

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.key)
        inorder(tree.right)

def print_expr(tree):
    result = ""
    if tree:
        result = "(" + print_expr(tree.left)
        result = result + str(tree.key)
        result = result + print_expr(tree.right) + ")"
    return result

