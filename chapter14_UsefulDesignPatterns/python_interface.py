from abc import ABCMeta, abstractclassmethod

class Pushable(metaclass=ABCMeta):
    @abstractclassmethod
    def push(self, x):
        """
        :param x:distance
        :return:
        """
class DummyPushable(Pushable):
    def push(self, x):
        return

class IncompletePushable(Pushable):
    pass

DummyPushable()
IncompletePushable()