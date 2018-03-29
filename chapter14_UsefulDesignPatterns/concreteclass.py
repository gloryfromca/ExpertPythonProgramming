if __name__ == "__main__":
    from Singleton import Singleton
else:
    from .Singleton import Singleton

class ConcreteClass(Singleton):
    pass

#print(Singleton())
#print(ConcreteClass())

print(ConcreteClass())
print(Singleton())
