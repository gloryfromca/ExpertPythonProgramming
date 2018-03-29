print("each object has __dict__ except basic data type:")
class s(object):
    pass
print(s().__dict__)
#print("sss".__dict__)
#print((2).__dict__)

print("\nattr of instance covers attr of class:")
class Myclass(object):
    x = 20
    def __init__(self):
        self.x = 10
print(Myclass.x)
print(Myclass().x)
print(Myclass.x)

print("\ndifferent descriptors:")
class data_attr_set_pass(object):
    def __init__(self, inner=None, name=""):
        self.inner = inner
        self.name = name
    def __get__(self, instance, owner):
        return self.inner
    def __set__(self, instance, value):
        pass
    def __repr__(self):
        return str(self.name) + ":" + str(self.inner)


class data_attr(object):
    def __init__(self, inner=None, name=""):
        self.inner = inner
        self.name = name
    def __get__(self, instance, owner):
        return self.inner
    def __set__(self, instance, value):
        self.inner = value
    def __repr__(self):
        return str(self.name) + ":" + str(self.inner)

class non_data_attr(object):
    def __init__(self, inner=None, name=""):
        self.inner = inner
        self.name = name
    def __get__(self, instance, owner):
        return self.inner
    def __repr__(self):
        return str(self.name) + ":" + str(self.inner)

class Myclass(object):
    x = data_attr_set_pass(11, "class attr")
    def __init__(self):
        self.__dict__["x"] = 2
print(Myclass.x)
m = Myclass()
print(Myclass.x)
print(m.x)
print(Myclass.__dict__)
print(m.__dict__)


print('================')
class Myclass(object):
    x = data_attr_set_pass(1324, "class attr")
    def __init__(self):
        self.x = 2232
print(Myclass.x)
m = Myclass()
print(Myclass.x)
print(m.x)
print(Myclass.__dict__)
print(m.__dict__)

print('================')
class Myclass(object):
    x = data_attr(14, "class attr")
    def __init__(self):
        self.__dict__["x"] = 28
print(Myclass.x)
m = Myclass()
print(Myclass.x)
print(m.x)
print(Myclass.__dict__)
print(m.__dict__)

print('================')
class Myclass(object):
    x = data_attr(121, "class attr")
    def __init__(self):
        self.x = 22
print(Myclass.x)
m = Myclass()
print(Myclass.x)
print(m.x)
print(Myclass.__dict__)
print(m.__dict__)

print('================')
class Myclass(object):
    x = non_data_attr(19, "class attr")
    def __init__(self):
        self.x = 27
print(Myclass.x)
m = Myclass()
print(Myclass.x)
print(m.x)
print(Myclass.__dict__)
print(m.__dict__)

print('strange=========')
class Myclass(object):
    x = data_attr_set_pass(11, "class attr")
    def __init__(self):
        self.x = data_attr(4412, "instance attr")
print(Myclass.x)
m = Myclass()
print(Myclass.x)
print(m.x)
print(Myclass.__dict__)
print(m.__dict__)

print('================')
class Myclass(object):
    x = data_attr(17, "class attr")
    def __init__(self):
        self.x = data_attr(5, "instance attr")
print(Myclass.x)
m = Myclass()
print(Myclass.x)
print(m.x)
print(Myclass.__dict__)
print(m.__dict__)

print("\ngetting descriptor in __dict__ won't call its __get__:")
class Myclass(object):
    x = 3
    def __init__(self):
        self.x = data_attr(8, "instance attr")
print(Myclass.x)
m = Myclass()
print(m.x)
print(Myclass.x)
print(Myclass.__dict__)
print(m.__dict__)
