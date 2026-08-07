from ADT import BinaryTree
from ADT import Stack
import operator

def makeTokens(expr):
    token_list = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ' or expr[i] == '\t':
            pass
        elif (expr[i] == 'a' or expr[i] == 'A') and (i+1 < len(expr) and (expr[i+1] == 'n' or expr[i+1] == 'N') and (i+2 < len(expr) and (expr[i+2] == 'd' or expr[i+2] == 'D'))):
            token_list.append('A')
            i += 2
        elif (expr[i] == 'o' or expr[i] == 'O') and (i+1 < len(expr) and (expr[i+1] == 'r' or expr[i+1] == 'R')):
            token_list.append('O')
            i += 1
        elif (expr[i] == 'n' or expr[i] == 'N') and (i+1 < len(expr) and (expr[i+1] == 'o' or expr[i+1] == 'O') and (i+2 < len(expr) and (expr[i+2] == 't' or expr[i+2] == 'T'))):
            token_list.append('N')
            i += 2
        elif not expr[i].isdigit():
            token_list.append(expr[i])
        else:
            num = ""
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            i -= 1
            token_list.append(num)
        i += 1
    return token_list

def build_parse_tree(expr):
    fp_list = makeTokens(expr)
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == '(':
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in ['+','-','*','/','A','O','N']:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i.isdigit():
            current_tree.root = int(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError("unknown operator")
        
    return expr_tree

def eval(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "A": operator.and_,
        "O": operator.or_,
        "N": operator.not_
    }

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()
    if left_child and right_child:
        fn = operators[parse_tree.root]
        return fn(eval(left_child), eval(right_child))
    else:
        return parse_tree.root


pt = build_parse_tree("(0 and 1)")
print(eval(pt))