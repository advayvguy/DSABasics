def print_expr(root):
    expr = ""
    if root:
        if root.left is None and root.right is None:
            return root.value.value
        else:
            expr = "(" + print_expr(root.left)
            if root.value.value != '*':
                expr += root.value.value
            expr += print_expr(root.right) + ")"
        return expr
    