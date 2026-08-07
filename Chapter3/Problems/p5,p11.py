from ADT import Stack

def perform_op(stack, token):
    print("token:", token)
    if (stack.size() < 2):
        raise ValueError("Error: too little to pop")
    s2 = stack.pop()
    s1 = stack.pop()
    if token == '+':
        stack.push(s1 + s2)
    elif token == '-':
        stack.push(s1-s2)
    elif token == '*':
        stack.push(s1 * s2)
    elif token == '/':
        if s2 == 0:
            raise ValueError("Error: Division by a zero")
        stack.push(s1/s2)

def postfix_eval(input_list):
    token_list = input_list.split()
    op_stack = Stack()

    for token in token_list:
        if token in "0123456789":
            op_stack.push(int(token))        
        else:
            perform_op(op_stack, token)
        print(op_stack._list)

    if op_stack.size() != 1:
        raise ValueError("Invalid postfix expression")

    return op_stack.pop()
    
postfix_eval("1 2 3 4 5 * + * +")
