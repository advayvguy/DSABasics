from ADT import Stack

def bracket_check(array):
    bstack = Stack()
    for i in array:
        if i == '(':
            bstack.push(1)
        elif i == ')':
            if bstack.is_empty():
                raise ValueError("invalid infix syntax: bracket error")
            bstack.pop()

    if not bstack.is_empty():
        raise ValueError("invalid infix syntax: bracket error")

def infix_check(a, pmap):
    current = a[0]

    if (current in pmap) and current != '(':
        raise ValueError("invalud infix syntax:  operator at the beginning")

    for i in range(len(a) - 1):
        curr = a[i]
        next = a[i+1]

        if curr in pmap and curr != '(': # if its + - / *
            if ((next in pmap) and next != '(') or next == ')': #if lookahead is + - / * )
                raise ValueError("invalid infix syntax: operator mismatch")
        elif curr not in pmap and curr != ')':      #ABC...    
            if (next not in pmap or next == '(') and next != ')':
                raise ValueError("invalid infix syntax: operand mismatch")
        elif curr == '(':
            if next in pmap and next != '(':
                raise ValueError("invalud infix syntax: operator mismatch")
        elif curr == ')':
            if next not in pmap and next != ')':
                raise ValueError("invalud infix syntax: operand mismatch")

    if a[-1] in pmap and a[-1] != ')':
         raise ValueError("Invalid infix syntax: Ends with operator")

def infix_to_postfix(input):
    token_list = input.split()
    #hashmap for priorities-
    op_stack = Stack()
    #priorities-
    priority_map = {}
    priority_map["^"] = 4
    priority_map["*"] = 3
    priority_map["/"] = 3
    priority_map["+"] = 2
    priority_map["-"] = 2
    priority_map["("] = 1
    output_list = []
    
    bracket_check(token_list)
    infix_check(token_list, priority_map)

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz":
            output_list.append(token)

        elif token == '(':
            op_stack.push('(')

        elif token == ')':
            stack_val = op_stack.pop()
            while stack_val != '(':
                output_list.append(stack_val)
                stack_val = op_stack.pop()

        elif token in priority_map:
            while (not op_stack.is_empty() and priority_map[op_stack.peek()] >= priority_map[token]):
                output_list.append(op_stack.pop())

            op_stack.push(token)

        else:
            raise ValueError("Invalid Character")

    while not op_stack.is_empty():
            output_list.append(op_stack.pop())

    return output_list

def perform_op(stack, token):
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
    elif token == '^':
        stack.push(s1 ** s2)

def postfix_eval(input_list):
    token_list = input_list
    op_stack = Stack()

    for token in token_list:
        if token in "0123456789":
            op_stack.push(int(token))        
        else:
            perform_op(op_stack, token)

    if op_stack.size() != 1:
        raise ValueError("Invalid postfix expression")

    return op_stack.pop()

def calculator(infix_input):
    postfix_input = infix_to_postfix(infix_input)
    return postfix_eval(postfix_input) 

print(calculator("2 + 3 * 3 + ( 4 * 4 ) ^ 2"))
