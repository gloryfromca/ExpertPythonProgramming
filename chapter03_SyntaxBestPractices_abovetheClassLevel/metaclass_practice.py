from collections import OrderedDict
class MetaclassA(type):
    @classmethod
    def __prepare__(mcls, name, bases):
        print("in __prepare__")
        print("mcls: " + str(mcls))
        return OrderedDict()

    def __new__(mcls, name, bases, attrs):
        print("in __new__")
        print("mcls: " + str(mcls))
        print("attrs in __new__:")
        print(attrs)
        return super().__new__(mcls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print("in __init__")
        print("cls: " + str(cls))


class A(object, metaclass=MetaclassA):
    s = 1
    a = 4
    def __new__(cls, *args, **kwargs):
        print("in instance's __new__")
        print(cls)
        return super().__new__(cls)

    def __init__(self):
        print("in instance's __init__")
        print(self)

A()
print(A.__dict__)