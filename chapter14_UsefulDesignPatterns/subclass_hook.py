from abc import ABCMeta, abstractclassmethod

class Pushable(metaclass=ABCMeta):
    @abstractclassmethod
    def push(self, x):
        """
        :param x:distance
        :return:
        """
    @classmethod
    def __subclasshook__(cls, c):
        if cls is Pushable:
            if any("push" in B.__dict__ for B in c.__mro__):
                return True
            return NotImplemented

class SomethingWithPush():
    def push(self, x):
        return
print(isinstance(SomethingWithPush(), Pushable))
