# Higher Order Functions
![[disc02.pdf]]

[[CS61A]]

## Higher Order Functions
**HOF**
```python
def compose(f, g):
	def h(x):
		return f(g(x))
	return h
"""f(g) doesn't work, since there are no arguments
so introducing an argument by new function and removing it by return value is a must"""
```

### A note
`lambda` expressions can be used as an *operator* or an *operand* to a call expression, unlike `def` statements.
```python
>>> (lambda f, x: f(x))(lambda y: y + 1, 10)
11
```

### Currying
```python
>>> def curried_pow(x):
		def h(y):
			return pow(x, y)
		return h
>>> curried_pow(2)(3)
8
```

### Questions
1.2

`def`:
```python
def curry2(h):
	def f(x):
		def g(y):
			return h(x, y)
		return g
	return f
```

`lambda`:
```python
curry2 = lambda h: lambda x: lambda y: h(x, y)
```

## Writing Higher Order Functions
1.5 Write a function that takes in a function cond and a number n and prints numbers from 1 to n where calling cond on that number returns True.

```python
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
```

1.6 Write a function similar to `keep_ints` like before, but now it takes in anumber $n$ and returns a function that has one parameter $cond$. The returned functions prints out numbers from 1 to n where calling cond on that number returns $True$.

```python
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
```

## Self-Reference
1.7 Write a function `print_delayed` delays printing its argument until the next function call. `print_delayed` takes in an argument $x$ and returns a new function `delay_print`. When `delay_print` is called, it prints out $x$ and returns another `delay_print`.

```python
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
```


1.8 Write a function `print_n` that can take in an integer $n$ and returns a repeatable print function that can print the next n parameters. After the nth parameter, it just prints "done".

```python
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
```


