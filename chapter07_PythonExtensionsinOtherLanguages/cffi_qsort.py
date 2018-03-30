from random import shuffle
from cffi import FFI

ffi = FFI()

ffi.cdef("""
    void qsort (void *base, size_t nel, size_t width, 
    int (*compar) (const void *, const void *));
""")

c = ffi.dlopen(None)

@ffi.callback("int (void *, void *)")
def ctypes_int_compare(a, b):
    # the type of int_is <class 'int'>
    int_a = ffi.cast("int*", a)[0]
    int_b = ffi.cast("int*", b)[0]
    return int_a - int_b

numbers = list(range(5))
shuffle(numbers)
print("shuffled: ", numbers)

c_array = ffi.new("int []", numbers)

c.qsort(
    #int []
    c_array,

    # len of c_array
    len(c_array),

    #the size of c_int
    ffi.sizeof("int"),

    # c-wrapper of a python func
    ctypes_int_compare,

)
print("sorted: ", list(c_array))
