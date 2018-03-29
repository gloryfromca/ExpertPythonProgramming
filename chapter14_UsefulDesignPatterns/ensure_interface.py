from abc import ABCMeta, abstractmethod, abstractproperty
import inspect
from functools import wraps
class IRectangle(metaclass=ABCMeta):
    @abstractproperty
    def width(self):
        return
    @abstractmethod
    def area(self):
        """
        :return:area
        """
    @classmethod
    def __subclasshook__(cls, c):
        if cls is IRectangle:
            if all([
                any("width" in B.__dict__ for B in c.__mro__),
                any("area" in B.__dict__ for B in c.__mro__),
            ]):
                return True
        return NotImplemented

def ensure_interface(function):
    signature = inspect.signature(function)
    params = signature.parameters

    @wraps(function)
    def worker(*args, **kwargs):
        bound = signature.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            annotation = params[name].annotation
            if not isinstance(annotation, ABCMeta):
                continue
            if not isinstance(value, annotation):
                raise TypeError(
                    "{} don't implement {} interface".format(value, annotation)
                )
        function(*args, **kwargs)
    return worker

@ensure_interface
def draw_rectangle(rectangle: IRectangle):
    print("I'm OK!")

draw_rectangle("foo")




