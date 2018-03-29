def s0():
    return 1
def s1():
    return 1,
def s2():
    return 1, 2
def s3():
    return (1, 2)
for i in [s0(), s1(), s2(), s3()]:
    print(i)
    print(type(i))


