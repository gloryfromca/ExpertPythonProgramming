class base(object):
    def __init__(self):
        print(base.__name__)
        super().__init__()

class A(base):
    def __init__(self):
        print(A.__name__)
        super().__init__()

class B(base):
    def __init__(self):
        print(B.__name__)
        super(B, self).__init__()

class C(A, B):
    def __init__(self):
        print(self.__class__.__name__)
        A.__init__(self)
        print("=======")
        B.__init__(self)

C()

