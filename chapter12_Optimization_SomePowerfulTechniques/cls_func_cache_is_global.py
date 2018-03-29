

def Cached(function):
    cached = {}
    def worker(self, n):
        try:
            result = cached[n]
        except Exception as e:
            print("worker is working!")
            result = cached[n] = function(self, n)
        finally:
            return result
    return worker


class CachedClass(object):
    def __init__(self, id):
        self.id = id

    @Cached
    def fibonacci(self, n):
        print("fibonacci is working!")
        if n < 2:
            return 1
        else:
            #self.fibonacci is Cached.
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

cc = CachedClass(10)
print(cc.fibonacci(4))
print(cc.fibonacci(5))
print(cc.fibonacci(3))
print("===================")
c2 = CachedClass(9)
print(cc.fibonacci(4))
print(cc.fibonacci(5))
print(cc.fibonacci(3))


