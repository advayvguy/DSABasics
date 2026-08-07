from stack import Stack

'''
    design-
        create an empty stack- opstack for storing the operators
        create an empty list for output 
        convert input string to a list -> tokens
        there will be a lookahead stage (peeking to check for the priority of the next token)

        key idea- if lookup < token -> we push the operator on the stack
                  otherwise, we start popping them until the lookup becomes lesser than the token

        when "(" is encounterd, nothing below it gets popped, it acts like a barricade of sorts, pretty neat
'''

def infix_to_postfix(input):
    token_list = input.split()

    #priority order
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec['-'] = 2
    prec["+"] = 2
    prec["("] = 1 #initial stuff stays on the stack until you get a closed braces

    op_stack = Stack()
    token_list = input.split() #reminds me of the k&r days where it was a pain to make a decent tokenizer
    post_fix = []

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
            post_fix.append(token)
        
        elif token == "(":
            op_stack.push(token)

        elif token == ")":
            top_token = op_stack.pop()
            while (top_token != "("):
                post_fix.append(top_token)
                top_token = op_stack.pop()
        else:
            while ((not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token])):
                post_fix.append(op_stack.pop())
            op_stack.push(token)

    while(not op_stack.is_empty()):
        post_fix.append(op_stack.pop())

    return "".join(post_fix)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("A + B"))
print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))
