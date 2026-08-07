from lexer import Token, Lexer
from BinaryTree import Stack, Node

def getprecedence(token):
    match token.value:
        case '+' | '-':
            return 0
        case '*' | '/':
            return 1
        case '^':
            return 2
        case '(':
            return -1 #no operator has a lesser value than this so '(' always sticks 

def Shunting_yard(tokenStream):
    operator = Stack()
    output = []

    for token in tokenStream:
        if token.type in ("VARIABLE","CONSTANT"):
            output.append(token)
        
        elif token.type == 'OPENBRACES':
            operator.push(token)
        
        elif token.type == 'CLOSEBRACES':
            while operator.size() > 0 and operator.peek().type != 'OPENBRACES':
                output.append(operator.pop())
            operator.pop()
            if operator.size() > 0 and operator.peek().type == 'FUNCTION':
                output.append(operator.pop())
        
        elif token.type == 'FUNCTION':
            operator.push(token)

        elif token.type == 'OPERATOR':
            #if token is exponent
            if token.value == '^':
                operator.push(token) #regardless of anyting you push it
            else:
                while operator.size() > 0 and operator.peek().type == 'OPERATOR' and getprecedence(operator.peek()) >= getprecedence(token):
                    output.append(operator.pop())
                operator.push(token)
    
    while operator.size() > 0:
        output.append(operator.pop())

    return output

def build_ast(postFix):
    stack = Stack()
    for token in postFix:
        if token.type in ['VARIABLE', 'CONSTANT']:
            stack.push(Node(token))
        elif token.type == 'FUNCTION':
            n = stack.pop()
            opnode = Node(token)
            opnode.left = n
            stack.push(opnode)
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            opnode = Node(token)
            opnode.left = n2
            opnode.right = n1
            stack.push(opnode)
    return stack.pop()
'''
expr = "sin(sin(sin(ln(x))))"
tokenStream = Lexer(expr)
print(Shunting_yard(tokenStream))
'''