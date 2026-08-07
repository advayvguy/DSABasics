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

def sindiff(root):
    top = Node(Token('*', 'OPERATOR'))
    top.left = differentiator(copyRecursive(root.left))
    top.right = Node(Token('cos', 'FUNCTION'))
    top.right.left = root.left
    return top

def cosdiff(root):
    top = Node(Token('*', 'OPERATOR'))
    top.left = Node(Token('-1', 'CONSTANT'))
    top.right = Node(Token('*', 'OPERATOR'))
    top.right.left = differentiator(copyRecursive(root.left))
    top.right.right = Node(Token('sin', 'FUNCTION'))
    top.right.right.left = root.left
    return top

def lndiff(root):
    top = Node(Token('/', 'OPERATOR'))
    top.left = differentiator(copyRecursive(root.left))
    top.right = root.left
    return top

def powdiff(root):
    f = root.left
    g = root.right
    top = Node(Token('*', 'OPERATOR'))
    top.left = Node(Token('^', 'OPERATOR'))
    top.left.left = copyRecursive(f)
    top.left.right = copyRecursive(g)
    top.right = Node(Token('+', 'OPERATOR'))
    top.right.left = Node(Token('*', 'OPERATOR'))
    top.right.right = Node(Token('*', 'OPERATOR'))
    top.right.left.left = differentiator(copyRecursive(g))
    top.right.left.right = Node(Token('ln', 'FUNCTION'))
    top.right.left.right.left = copyRecursive(f)
    top.right.right.left = copyRecursive(g)
    top.right.right.right = Node(Token('/', 'OPERATOR'))
    top.right.right.right.left = differentiator(copyRecursive(f))
    top.right.right.right.right = copyRecursive(f)
    return top

def tandiff(root):
    x = root.left
    top = Node(Token('*', 'OPERATOR'))
    top.left = differentiator(copyRecursive(x))
    top.right = Node(Token('^', 'OPERATOR'))
    top.right.left = Node(Token('sec', 'FUNCTION'))
    top.right.left.left = copyRecursive(x)
    top.right.right = Node(Token('2', 'CONSTANT'))
    return top

def cotdiff(root):
    x = root.left
    top = Node(Token('*', 'OPERATOR'))
    top.left = Node(Token('-1', 'CONSTANT'))
    top.right = Node(Token('*', 'OPERATOR'))
    top.right.left = differentiator(copyRecursive(x))
    top.right.right = Node(Token('^', 'OPERATOR'))
    top.right.right.left = Node(Token('csc', 'FUNCTION'))
    top.right.right.right = Node(Token('2', 'CONSTANT'))
    top.right.right.left.left = copyRecursive(x)
    return top

def secdiff(root):
    x = root.left
    top = Node(Token('*', 'OPERATOR'))
    top.left = differentiator(copyRecursive(x))
    top.right = Node(Token('*', 'OPERATOR'))
    top.right.left = Node(Token('sec', 'FUNCTION'))
    top.right.right = Node(Token('tan','FUNCTION'))
    top.right.left.left = copyRecursive(x)
    top.right.right.left = copyRecursive(x)
    return top

def cscdiff(root):
    x = root.left
    top = Node(Token('*', 'OPERATOR'))
    top.left = Node(Token('-1', 'CONSTANT'))
    top.right = Node(Token('*', 'OPERATOR'))
    top.right.left = differentiator(copyRecursive(x))
    top.right.right = Node(Token('*', 'OPERATOR'))
    top.right.right.left = Node(Token('csc', 'FUNCTION'))
    top.right.right.right = Node(Token('cot', 'FUNCTION'))
    top.right.right.left.left = copyRecursive(x)
    top.right.right.right.left = copyRecursive(x)
    return top

def differentiator(root):
    if root.value.type == 'FUNCTION':
        if root.value.value == 'sin':
            root = sindiff(root)
        elif root.value.value == 'cos':
            root = cosdiff(root)
        elif root.value.value == 'ln':
            root = lndiff(root)
        elif root.value.value == 'csc':
            root = cscdiff(root)
        elif root.value.value == 'sec':
            root = secdiff(root)
        elif root.value.value == 'tan':
            root = tandiff(root)
        elif root.value.value == 'cot':
            root = cotdiff(root)
    elif root.value.value == '^':
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
        else:
            root = powdiff(root)
        
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