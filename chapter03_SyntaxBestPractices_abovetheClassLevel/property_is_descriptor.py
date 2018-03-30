class Rectangle(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    @property
    def width(self):
        return self.x2 - self.x1
    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value
r = Rectangle(0, 0, 1, 1)
print(r.width)
r.width = 10
print(r.width)
