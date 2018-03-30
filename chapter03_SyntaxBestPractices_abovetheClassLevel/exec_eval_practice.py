class A(object):
    def __init__(self):
        exec("self.x = 3")
        self.y = eval("100*10")
a = A()
print(a.x)
print(a.y)
print(a.__dict__)
print("================")
goal = {"age": 1}
locl = {}
exec("abc = age + 1 ", goal, locl)
print(goal)
print(locl)
print("================")
goal = {}
locl = {"age": 1}
exec("abc = age + 1 ", goal, locl)
print(goal)
print(locl)

