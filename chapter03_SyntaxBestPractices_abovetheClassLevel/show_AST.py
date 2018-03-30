import ast

tree = ast.parse(
"""
class A(object):
    pass
"""
)
print(tree)
print(ast.dump(tree))
