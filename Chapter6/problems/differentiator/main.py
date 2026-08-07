from lexer import Lexer
from simplifier import simplifier
from AST import Shunting_yard, build_ast
from differentiator import differentiator
from evaluator import print_expr

expr = input("")

tokenStream = Lexer(expr)
postfixStream = Shunting_yard(tokenStream)
ast = build_ast(postfixStream)
simplifiedAst = simplifier(ast)
derivativeTree = differentiator(simplifiedAst)
simplifiedTree = simplifier(derivativeTree)
expr = print_expr(simplifiedTree)
print(expr)