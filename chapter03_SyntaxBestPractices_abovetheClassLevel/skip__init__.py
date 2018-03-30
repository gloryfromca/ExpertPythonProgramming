class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None
    def __init__(self, value):
        print("value is: " + str(value))
print(NonZero(1))

print('=============================')

class NonZero(int):
    def __new__(cls, value):
        return value if value != 0 else None
    def __init__(self, value):
        print("value is: " + str(value))
print(NonZero(1))