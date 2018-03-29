class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    def __init__(self):
        print("in __init__()")

instance_a = Singleton()
instance_b = Singleton()
print(instance_a == instance_b)

