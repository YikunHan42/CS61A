# HOF
def compose(f, g):
	def h(x):
		return f(g(x))
	return h
"""f(g) doesn't work, since there are no arguments
so introducing an argument by new function and removing it by return value is a must"""

# Currying
def curry2(h):
	def f(x):
		def g(y):
			return h(x, y)
		return g
	return f

curry2 = lambda h: lambda x: lambda y: h(x, y)

# Keep ints
def keep_ints(cond, n):
	"""Print out all integers 1..i..n where cond(i) is true

    >>> def is_even(x):
		    # Even numbers have remainder 0 when divided by 2.
		    return x % 2 == 0
	>>> keep_ints(is_even, 5)
	2
	4
	"""
	for i in range(1, n + 1):
		if cond(i): print(i)

# Make keeper
def make_keeper(n):
	"""Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.

	>>> def is_even(x):
			# Even numbers have remainder 0 when divided by 2.
			return x % 2 == 0
	>>> make_keeper(5)(is_even)
	2
	4
	"""
	def g(f):
		for i in range(1, n + 1):
			if f(i): print(i)
	return g

# Self Reference
def print_delayed(x):
	"""Returns a new function. This new function, when called, will print out x and return another functin with the same behavior.
	>>> f = print_delayed(1)
	>>> f = f(2)
	1
	>>> f = f(3)
	2
	>>> f = f(4)(5)
	3
	4
	>>> f("hi")
	5
	<function print_delayed> # a function is returned
	"""
	def delay_print(y):
		print(x)
		return print_delayed(y)
	return delay_print

def print_n(n):
	"""
	>>> f = print_n(2)
	>>> f = f("hi")
	hi
	>>> f = f("hello")
	hello
	>>> f = f("bye")
	done
	>>> g = print_n(1)
	>>> g("first")("second")("third")
	first
	done
	done
	<function inner_print>
	"""
	def inner_print(x):
		if n == 0:
			print("done")
		else:
			print(x)
		return print_n(n - 1)
	return inner_print