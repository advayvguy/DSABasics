import operator
from BinaryTree import Node
from lexer import Token

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def iszero(node):
    return node.value.type == 'CONSTANT' and float(node.value.value) == 0

def simplifier(root):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        return root

    root.left = simplifier(root.left)
    root.right = simplifier(root.right)
    
    #folding
    if (root.left.value.value != 'e' and (root.right is None or root.right.value.value != 'e')) and (root.left.value.type == 'CONSTANT' and (root.right is not None and root.right.value.type == 'CONSTANT')):
        n1 = Node(Token(str(operators[root.value.value](int(root.left.value.value), int(root.right.value.value))), 'CONSTANT'))
        return n1 
    
    #some other simplifications
    elif root.value.value == 'ln' and root.left.value.value == 'e':
        return Node(Token('1', 'CONSTANT'))
    elif root.value.value == '+' or root.value.value == '-':
        if root.left.value.value == '0' and root.value.value == '+':
            return root.right
        elif root.right.value.value == '0':
            return root.left
    elif root.value.value == '*':
        if iszero(root.left) or iszero(root.right):
            return Node(Token('0', 'CONSTANT'))
        elif root.left.value.value == '1':
            return root.right
        elif root.right.value.value == '1':
            return root.left
    elif root.value.value == '/':
        if root.right.value.value == '1':
            return root.left
        elif root.left.value.value == '0':
            return Node(Token('0', 'CONSTANT'))
        elif root.right.value.value == '0':
            raise ValueError("error: division by 0")
    elif root.value.value == '^':
        if root.right.value.value == '1':
            return root.left
        elif root.right.value.value == '0':
            return Node(Token('1', 'CONSTANT'))

    return root