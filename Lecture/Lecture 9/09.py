# Assert
def fact(x):
	assert isinstance(x, int)
	assert x >= 0
	if x == 0:
		return 1
	else:
		return x * fact(x - 1)
def half_fact(x):
	return fact(x / 2)

# Taylor
def t(f, n, x, x0 = 0):

	r = 0
	while n:
		r += (x - x0) ** n / fact(n) * d(n, f)(x0)
		n -= 1
	return r

# Traceback
def f(x):
	1 / 0
def g(x):
	f(x)
def h(x):
	g(x)
print(h(2))

# Handling Exceptions
try:
	x = 1 / 0
except ZeroDivisionError as e:
	print('handling a', type(e))
	x = 0

# Invert
def invert(x):
	y = 1 / x
	print('Never printed if x is 0')
	return y

def invert_safe(x):
	try:
		return invert(x)
	except ZeroDivisionError as e:
		print('handled', e)
		return 0

def invert(x):
	result = 1 / x
	print('Never printed if x is 0')
	return result

def invert_safe(x):
	try:
		return invert(x)
	except ZeroDivisionError as e:
		return str(e)

from operator import add, mul, truediv

def divide_all(n, ds):
	try:
		return reduce(truediv, ds, n)
	except ZeroDivisionError:
		return float('inf')

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).

    >>> reduce(mul, [2, 4, 8]), 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).

    >>> reduce(mul, [2, 4, 8]), 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))
