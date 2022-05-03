# Control
[[CS61A]]
![[03-Control_1pp.pdf]]

## Print and None
Difference between **printing** and **evaluating**
```python
# Print
-2
print(-2)
'Go Bears'
print('Go Bears')
print(1, 2, 3)
None
print(None)
x = -2
x
x = print(-2)
x
print(print(1), print(2))
```
`print(print(1), print(2))`actually returns
1
2
None None

### None
None indicates that nothing is returned
A function that does not explicitly return a value will return None
**None is not displayed by the interpreter as the value of an expression**

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205011505779.png)

### Pure Functions & Non-Pure Functions
Pure Functions: close pipe
Non-pure Functions: have side effects
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205011507899.png)
similar to **leaks**?

### Nested Expressions with Print
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205011508471.png)
Since **None is not displayed by the interpreter as the value of an expression**, the third **None** is not displayed

## Miscellaneous Python Features
```python
# Addition/Multiplication
2 + 3 * 4 + 5 # add, mul
(2 + 3) * (4 + 5)

# Division
618 / 10
618 // 10
618 % 10
from operator import truediv, floordiv, mod
floordiv(618, 10)
truediv(618, 10)
mod(618, 10)

# Approximation
5 / 3 # truediv
5 // 3 # floordiv
5 % 3 # mod

# Multiple return values
def divide_exact(n, d):
    return n // d, n % d
quotient, remainder = divide_exact(618, 10)

# Dostrings, doctests, & default arguments
def divide_exact(n, d=10): # d = 10 if it's not filled
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(618, 10)
    >>> quotient
    61
    >>> remainder
    8
    """
    return floordiv(n, d), mod(n, d)
# simulate the session(python -m doctest -v name.py)
```

## Conditional Statements
A *statement* is executed by the interpreter to perform an action

abs:
```python
# Conditional expressions
def absolute_value(x):
    """Return the absolute value of X.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
```

`if` and `elif` and `else` 

### Boolean Contexts
**True** & **False**
False: False, 0, '', None
True: Anything else

## Iteration
### While Statements

```python
# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
total
```

### Iteration Example
#### The Fibonacci Sequence
```python
def fib(n):
	"""Compute the nth Fibonacci number, for N >= 1."""
	pred, curr = 0, 1 # 0th and 1st Fibonacci numbers
	k = 1             # curr is the kth Fibonacci number
	while k < n:
		pred, curr = curr, pred + curr
	return curr
```

A substitute which can calculate the 0th number correctly
```python
def fib(n):
	"""Compute the nth Fibonacci number, for N >= 1."""
	pred, curr = 1, 0
	k = 0
	while k < n:
		pred, curr = curr, pred + curr
	return curr
```

## Return
### Return Statements
Only one return statement is ever executed while executing the body of a function
```python
# Return

def end(n, d):
    """Print the final digits of N in reverse order until D is found.

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None
```

```python
def search(f): # f is a function, not number, such as search(positive) = 11
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def is_three(x):
    """Return whether x is three.

    >>> search(is_three)
    3
    """
    return x == 3

def square(x):
    return x * x

def positive(x):
    """A function that is 0 until square(x)-100 is positive.

    >>> search(positive)
    11
    """
    return max(0, square(x) - 100)

def invert(f):
    """Return a function g(y) that returns x such that f(x) == y.

    >>> sqrt = invert(square)
    >>> sqrt(16)
    4
    """
    return lambda y: search(lambda x: f(x) == y) # inverse function, only for perfect square
    # lambda(a : b) means a is the operand, and b is the return value
	# return lambda y: search(lambda x: square(x) == y)
	# return lambda y: sqrt(y)
	# f = sqrt ?
```

## Designing Functions
domain & range
A pure function's behavior is the **relationship** it creates between input and output

### A Guide
+ Give each functions exactly one job
+ Don't repeat yourself. Implement once, but execute it many times
+ Define functions generally

## Control
### If Statements and Call Expressions
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205011631019.png)

```python
# Control

def if_(c, t, f):
    if c:
        t
    else:
        f
```

**Example of Evaluation Rule**
```python
from math import sqrt

def real_sqrt(x):
    """Return the real part of the square root of x.

    >>> real_sqrt(4)
    2.0
    >>> real_sqrt(-4)
    0.0
    """
    if x > 0:
        return sqrt(x)
    else:
        return 0.0
    # if_(x > 0, sqrt(x), 0.0) # call expression, all three of these are evaluated before if and else statements are recalled 
    # so real_sqrt(-4) will not work
```

## Control Expressions
### Logical Operators
`and` `or`

```python
# Control Expressions

def has_big_sqrt(x):
    """Return whether x has a big square root.

    >>> has_big_sqrt(1000)
    True
    >>> has_big_sqrt(100)
    False
    >>> has_big_sqrt(0)
    False
    >>> has_big_sqrt(-1000)
    False
    """
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    """Is N small enough that 1/N can be represented?

    >>> reasonable(100)
    True
    >>> reasonable(0)
    True
    >>> reasonable(-100)
    True
    >>> reasonable(10 ** 1000)
    False
    """
    return n == 0 or 1/n != 0.0
```

### Condtional Expressions
<consequent> if <predicate> else <alternative>





