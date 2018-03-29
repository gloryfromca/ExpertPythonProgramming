class A(object):
    @classmethod
    def do_your_stuff(cls):
        print('This is A')
    def __repr__(self):
        print("in baseclass' __repr__")
        return self.__class__.__name__ + "'s instance"

class B(A):
    @classmethod
    def do_your_stuff(cls):
        super(B, cls).do_your_stuff()
    def __repr__(self):
        # arg:self of __repr__() is B's instance, but __repr__() is bounded to baseclass.
        return super().__repr__()


B.do_your_stuff()
print("===============================")
print(A())
print(B())