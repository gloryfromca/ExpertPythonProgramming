from random import shuffle
import ctypes
from ctypes.util import find_library

#find and load standard c library.
libc = ctypes.cdll.LoadLibrary(find_library("c"))

CMPFUNC = ctypes.CFUNCTYPE(
    # return value
    ctypes.c_int,

    # first param
    ctypes.POINTER(ctypes.c_int),

    # second param
    ctypes.POINTER(ctypes.c_int),
)

def ctypes_int_compare(a, b):
    # a and b are pointers.
    # the type of a is class '__main__.LP_c_int'>
    print("%s cmp %s" % (a[0], b[0]))
    return a[0] - b[0]

numbers = list(range(5))
shuffle(numbers)
print("shuffled: ", numbers)

NumbersArray = ctypes.c_int * len(numbers)
c_array = NumbersArray(*numbers)

libc.qsort(
    #ctype
    c_array,

    # len of c_array
    len(c_array),

    #the size of c_int
    ctypes.sizeof(ctypes.c_int),

    # c-wrapper of a python func
    CMPFUNC(ctypes_int_compare)

)
print("sorted: ", list(c_array))





