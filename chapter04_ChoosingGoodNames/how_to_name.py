# global constant
from doctest import IGNORE_EXCEPTION_DETAIL

#global mark
OPTIONS = {}

#package private variable
_observers = []

#class private variable
class Citizen(object):
    def __init__(self, age):
        self._age = age
    def get_age(self):
        return self._age

#method and func
import  datetime
def get_time():
    return datetime.datetime()

#class private func
class Base(object):
    def __secret(self):
        print("don't tell")
    def public(self):
        #this will always call _base__secret() whatever self is base_class or derived_class.
        self.__secret()
class Derived(Base):
    def __secret(self):
        print("never ever")
Derived().public()

#args
def a_method(my_name):
    pass

#class
class MyClass(object):
    pass

#module and package
import os

#boolean variable
is_connected = True
has_cache = False

#collections
users = {"z", "h"}
names = ["hui", "xu"]

#dict
persons_addresses = {"zhanghui": "ShangHai",
                     "zhangbo": "HeBei",
                     }

#avoid generic name
names_should_avoid = ["manager", "object", "handle", "do"]

#creating names should be avoiding exist names
os = 1
import os
print(os)

#protocol implementation
import urllib














