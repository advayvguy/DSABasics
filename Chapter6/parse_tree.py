from ADT import BinaryTree
from ADT import Stack
import operator

def build_parse_tree(expr):
    fp_list = expr.split()
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == '(':
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in ['+','-','*','/']:
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
        "/": operator.truediv
    }

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()
    if left_child and right_child:
        fn = operators[parse_tree.root]
        return fn(eval(left_child), eval(right_child))
    else:
        return parse_tree.root


pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(eval(pt))