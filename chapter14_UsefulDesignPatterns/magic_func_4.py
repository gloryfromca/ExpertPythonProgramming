class meta_s(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, "in metaclass __prepare__")
        print(kwargs)
        return super().__prepare__(name, bases, **kwargs)

    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, "in metaclass __new__")
        print(kwargs)
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(cls, "in metaclass __init__")
        print(kwargs)

    def __call__(cls, *args, **kwargs):
        print(cls, "in metaclass __call__")
        print(args, kwargs)
        d = super().__call__(*args, **kwargs)
        print("metaclass __call__ return", d)
        return d

class s(object, metaclass=meta_s, extra="to_metaclass"):
    def __new__(cls, *args, **kwargs):
        print(cls, "in class __new__")
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(self, "in class __init__")
        print(args, kwargs)

    def __call__(self, *args, **kwargs):
        print(self, "in class __call__")
        print(args, kwargs)

    def __repr__(self):
        return "s_instance"

print("begin instance============")
a = s("to_class")
print("call on instance=============")
a("to_instance")
