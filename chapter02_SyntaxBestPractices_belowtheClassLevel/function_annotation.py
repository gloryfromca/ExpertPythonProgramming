def f(zhang: str, hui: str='name') -> str:
    return zhang+hui
print(f("zhang", "hui"))
print(f.__annotations__)
