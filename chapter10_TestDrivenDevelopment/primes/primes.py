import math
def is_prime(number):
    if type(number) is not int or number < 2:
        return False
    for element in range(2, int(math.sqrt(number))+2):
        if number % element == 0:
            return False
    return True