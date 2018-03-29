from functools import lru_cache
import time

def fibonacci_o(n):
    if n < 2:
        return 1
    else:
        return fibonacci_o(n - 1) + fibonacci_o(n - 2)
begin = time.time()
for i in range(10000):
    fibonacci_o(15)
end = time.time()
print("time of origin func:", end-begin)


@lru_cache(1280, True)
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

begin = time.time()
for i in range(10000):
    fibonacci(15)
end = time.time()
print("time of cached func:", end-begin)