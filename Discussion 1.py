# 1.1

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining == True: return True
    else: return False

def wears_jacket(temp, raining):
    return True if temp < 60 or raining == True else False

# 1.2

def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))
# endless while loop

# 1.3
from math import sqrt
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = 2
    while i <= sqrt(n):
        if(n % i == 0) : return False
        i += 1
    return True


