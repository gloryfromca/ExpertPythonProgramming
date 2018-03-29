class LazyClassProperty(object):
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        print("instance:", instance, ", owner:", owner)
        value = self.fget(instance or owner)
        setattr(owner, self.fget.__name__, value)
        return value

class HavingLazyClassProperty(object):

    @LazyClassProperty
    def initializedCostly(clsOrSelf):
        value = 1+2+34+34*8
        return value

print(HavingLazyClassProperty.__dict__)
expensiveValue = HavingLazyClassProperty.initializedCostly
print(expensiveValue)
expensiveValue = HavingLazyClassProperty().initializedCostly
print(expensiveValue)
print(HavingLazyClassProperty.__dict__)