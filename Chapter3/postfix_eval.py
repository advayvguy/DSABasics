from stack import Stack

def do_op(op1, op2, token):
    n1 = int(op1)
    n2 = int(op2)

    if token == "+":
        return str(n1 + n2)
    elif token == "-":
        return str(n1 - n2)
    elif token == '*':
        return str(n1 * n2)
    elif token == '/':
        if n2 == 0:
            raise ValueError("cannot divide with 0")
        return str(n1 / n2)
    else:
        raise RuntimeError("invalid operator")

def postfix_eval(input):
    token_list = input.split()
    num_stack = Stack()

    for token in token_list:

        if token in "0123456789":
            num_stack.push(token)
        else:
            op2 = num_stack.pop()
            op1 = num_stack.pop()
            op = do_op(op1, op2, token)
            num_stack.push(op)

    return num_stack.pop()

print(postfix_eval("7 8 + 3 2 + /"))
