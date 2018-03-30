def s():
    while True:
        yield 3
y3 = s()
print(next(y3))
print(next(y3))
print(next(y3))
print(next(y3))
print(next(y3))