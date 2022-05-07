# Environment Diagrams
[[CS61A]]
![[05-Environment_Diagrams_1pp.pdf]]

## Multiple Environments
### Life Cycle of a User-Defined Functions
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062130757.png)
**call expression: different from `#define` in C++**

### Multiple Environments in One Diagram
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062134861.png)
None of them include all the above **three** frames!

Name have no meanings without environment.

### Names Have Different Meanings in Different Environments
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062138094.png)
Still works(although not recommended), `square` is only defined as a function in global frame.

## Environments for Higher-Order Functions
*Environment diagrams describe how higher-order functions work!*

```python
# Functional arguments  
  
def apply_twice(f, x):  
    """Return f(f(x))  
  
    >>> apply_twice(square, 2)  
    16    >>> from math import sqrt    >>> apply_twice(sqrt, 16)  
    2.0    """    return f(f(x))  
  
def square(x):  
    return x * x  
  
result = apply_twice(square, 2)  
```

### Names can be Bound to Functional Arguments
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062157698.png)

## Higher-Order Function Example: Repeat
```python
def repeat(f, x):
	while f(x) != x:
		x = f(x)
	return x

def g(y):
	return (y + 5) // 3

result = repeat(g, 5)
	# x = 5 -> 3 -> 2
```

## Environments for Nested Definitions
### Environment Diagrams for Nested Def Statements
```python  
# Functional return values  
  
def make_adder(n):  
    """Return a function that takes one argument k and returns k + n.  
  
    >>> add_three = make_adder(3)    >>> add_three(4)  
    7    """    def adder(k):  
        return k + n  
    return adder  
# n, k = 3, 4
# Lexical scope and returning functions  
```

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062241866.png)
**The key point is here!**

### How to Draw an Environment Diagram
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062244192.png)

## Local Names
```python
def f(x, y):  
    return g(x)  
  
def g(a):  
    return a + y  
  
# This expression causes an error because y is not bound in g.  
# f(1, 2)  
```

Local names are not visible to other(non-nested) functions.

## Lambda Expressions
```python
# Lambda expressions  
  
x = 10  
square = x * x  
square = lambda x: x * x # return function, rather than number
# No "return" keyword!
# Value must be a single expression
square(4)  
```
Not common in Python, but important in general.
Cannot contain statements at all.

### Contrast of `lambda` and `def`
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062253337.png)

type of square on the left: function lambda
type of square on the right: function square

## Self-Reference
``` python
  
# Self Reference  
  
def print_all(k):  
    """Print all arguments of repeated calls.  
  
    >>> f = print_all(1)(2)(3)(4)(5)  
    1    2    3    4    5    """    print(k)  
    return print_all  
# print_all(1)(3)(5) -> print 1, 3, 5 in order

def print_sums(n):  
    """Print all sums of arguments of repeated calls.  
  
    >>> f = print_sums(1)(2)(3)(4)(5)  
    1    3    6    10    15    """    print(n)  
    def next_sum(k):  
        return print_sums(n+k)  
    return next_sum
# finally returns next_sum, which is a function without arguments, and it's done
```

## Midterm1 Review
### What Would Python Print?
`print` function returns $None$.

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062304462.png)

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062309901.png)
`pirate(x)` -> identity()
`pirate(pirate(pirate))(5)(7)` -> only 2 Matey
Nonintuitive concept again.

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205062314400.png)

## Decoraters
```python
from ucb import trace

def trace1(fn):
	"""Returns a version of fn
	fn - a function of 1 argument
	""" 
	def traced(x):
		print('Calling', fn, 'on argument', x)
		return fn(x)
	return traced

@trace1
def square(x):
	return x * x

# is identical to
def square(x):
	return x * x
sqaure = trace1(square)

@trace1
def sum_square_up_to(n):
	k = 1
	total = 0
	while k <= n:
		total, k = total + square(k), k + 1
	return total
```

## Code
```python
# Composition  
  
def compose1(f, g):  
    """Return a function that composes f and g.  
  
    f, g -- functions of a single argument    """    def h(x):  
        return f(g(x))  
    return h  
  
def triple(x):  
    return 3 * x  
  
squiple = compose1(square, triple)  
tripare = compose1(triple, square)  
squadder = compose1(square, make_adder(2))  
```

