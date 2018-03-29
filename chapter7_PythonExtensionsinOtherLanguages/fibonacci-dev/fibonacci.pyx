cdef long long fibonacci_cc(unsigned int n) nogil:
    if n < 2:
        return 99
    else:
        return fibonacci_cc(n-1) + fibonacci_cc(n-2)

# you must use def as proxy of cdef.
def fibonacci(unsigned int n):
        return fibonacci_cc(n)


