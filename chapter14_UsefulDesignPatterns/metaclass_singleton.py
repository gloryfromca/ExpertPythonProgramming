
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(cls)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class ConcreteClass(metaclass=Singleton):
    pass
class ConCreteSubClass(ConcreteClass):
    pass
print(ConcreteClass()==ConcreteClass())
print(ConCreteSubClass()==ConCreteSubClass())


