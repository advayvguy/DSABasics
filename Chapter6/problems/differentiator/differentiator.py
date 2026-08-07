from BinaryTree import Node
from AST import Token
#from copy import deepcopy

def helper(root):
    if root is None:
        return root
    
    node = Node(root.value)
    node.left = helper(root.left)
    node.right = helper(root.right)
    return node 

def copyRecursive(root):
    return helper(root)

def differentiator(root):
    if root.value.value == '^':
        if root.right.value.type == 'CONSTANT':
            num = root.right.value.value
            expr = root.left
            root.left = root.right
            root.right = Node(Token('*', 'OPERATOR'))
            root.right.right = Node(Token('^', 'OPERATOR'))
            root.right.right.right = Node(Token(str(int(num)-1), 'CONSTANT'))
            root.right.right.left = expr
            root.right.left = differentiator(copyRecursive(expr))
            root.value = Token('*', 'OPERATOR')
            return root 
        
    elif root.value.type == 'CONSTANT':
        return Node(Token('0', 'CONSTANT'))
    
    elif root.value.type == 'VARIABLE':
        return Node(Token('1', 'CONSTANT'))

    elif root.value.value == '+' or root.value.value == '-':
        root.left = differentiator(root.left) 
        root.right = differentiator(root.right)

    elif root.value.value == '*':
        root.value = Token('+', 'OPERATOR')
        u = copyRecursive(root.left)
        v = copyRecursive(root.right)
        root.left.value = Token('*', 'OPERATOR')
        root.right.value = Token('*', 'OPERATOR')
        root.left.left = u
        root.left.right = differentiator(copyRecursive(v))
        root.right.right = v
        root.right.left = differentiator(copyRecursive(u))

    elif root.value.value == '/':
        u = copyRecursive(root.left)
        v = copyRecursive(root.right)
        root.left.value = Token('-', 'OPERATOR')
        root.right.value = Token('^', 'OPERATOR')
        root.left.left = Node(Token('*', 'OPERATOR'))
        root.left.right = Node(Token('*', 'OPERATOR'))
        root.right.left = v
        root.right.right = Node(Token('2', 'CONSTANT'))
        root.left.left.left = differentiator(copyRecursive(u))
        root.left.left.right = v
        root.left.right.left = differentiator(copyRecursive(v))
        root.left.right.right = u

    return root 