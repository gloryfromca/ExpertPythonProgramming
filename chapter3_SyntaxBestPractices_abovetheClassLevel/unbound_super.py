class fruit():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    @classmethod
    def recommend(cls):
        print("baseclass' recommend(), cls is: " + str(cls))
        return [fruit("tangerine"), fruit("banana")]


class apple(fruit):
    def __init__(self):
        super(apple, self).__init__("apple")
    @classmethod
    def recommend(cls):
        print("cls is: " + str(cls))

        print()
        print("print super() operation:")
        print(super())
        print(super(apple))
        # super(apple, cls()) is same as super(apple, cls)
        print(super(apple, cls()))
        print(super(apple, cls))
        print()

        # recommend() belongs to baseclass of `apple`, arg cls will be `apple`.
        recommend_fruits = super().recommend()
        recommend_fruits = super(apple, cls).recommend()

        recommend_fruits.append(cls())
        return recommend_fruits

for i in [fruit.recommend(), ]:
    print(i)
print("===============================")
for i in [apple.recommend(), ]:
    print(i)


