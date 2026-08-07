def print_expr(root):
    expr = ""
    if root:
        if root.left is None and root.right is None:
            return root.value.value
        
        elif root.value.type == 'FUNCTION':
            expr = root.value.value + '(' + print_expr(root.left) + ')'

        elif root.value.value == '*' and (root.left.value.value == '-1' or root.right.value.value == '-1'):
            if root.left.value.value == '-1':
                expr = '-' + print_expr(root.right)
            elif root.right.value.value == '-1':
                expr = '-' + print_expr(root.left)
            
        else:
            expr = "(" + print_expr(root.left)
            if root.value.value != '*':
                expr += root.value.value
            expr += print_expr(root.right) + ")"
        return expr
    