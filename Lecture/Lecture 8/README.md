# Sequences & Data Abstraction
[[CS61A]]

## Lists
```python
# Lists  
  
odds = [41, 43, 47, 49]  
len(odds)  
odds[1]  
odds[0] - odds[3] + len(odds)  
odds[odds[3]-odds[2]]  
  
```

## Containers
Built-in operators for testing whether an element appears in a compound value

```python
# Containers  
  
digits = [1, 8, 2, 8]  
1 in digits  
'1' in digits  
[1, 8] in digits  
[1, 2] in [[1, 2], 3]  
# individual elements, not subsequences
```

## For Statements
```python
# For statements  
  
def count_while(s, value):  
    """Count the number of occurrences of value in sequence s.  
  
    >>> count_while(digits, 8)    2    """    total, index = 0, 0  
    while index < len(s):  
        if s[index] == value:  
            total = total + 1  
        index = index + 1  
    return total  
  
def count_for(s, value):  
    """Count the number of occurrences of value in sequence s.  
  
    >>> count_for(digits, 8)    2    """    total = 0  
    for elem in s:  
        if elem == value:  
            total = total + 1  
    return total 
```

### Sequence Unpacking in For Statements
```python
def count_same(pairs):  
    """Return how many pairs have the same element repeated.  
  
    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]    >>> count_same(pairs)    2    """    same_count = 0  
    for x, y in pairs: # as in multiple assignments  
        if x == y:
            same_count = same_count + 1  
    return same_count 
```

## Ranges
$Length$: ending value - starting value
$Element selection$: starting value + index

```python
# Ranges  
  
list(range(5, 8))  
list(range(4))  
len(range(4))  
  
def sum_below(n):  
    total = 0  
    for i in range(n):  
        total += i  
    return total  
  
def cheer():  
    for _ in range(3):  
        print('Go Bears!')
# _ means you will don't use this argument anywhere else  
```

## List Comprehensions
```python
# List comprehensions  
  
odds = [1, 3, 5, 7, 9]  
[x+1 for x in odds]
# returns [2, 4, 6, 8, 10]
[x for x in odds if 25 % x == 0]  
  
def divisors(n):  
    """Return the integers that evenly divide n.  
  
    >>> divisors(1)    [1]    >>> divisors(4)    [1, 2]    >>> divisors(12)    [1, 2, 3, 4, 6]    >>> [n for n in range(1, 1000) if sum(divisors(n)) == n]    [1, 6, 28, 496]    """    return [1] + [x for x in range(2, n) if n % x == 0]
# similar to string concat, rather than opeartor add  
```

## Strings

```python
exec('curry = lambda f: lambda x: lambda y: f(x, y)')
# similar to assigment
```

Single-quoted and double-quoted strings are equivalent
\: backslash

```python
city = 'Berkeley'
city[3]
# String to string
# List to numeral
```

## Data Abstraction
+ Compound objects combine objects together
+ A data
+ A geographic position
+ An abstract data type lets us manipulate compound objects as units
+ Isolate two parts of any program that uses data

### Rational Numbers
+ rational(n, d)
+ number(x)
+ denom(x)

Constructors and selectors
```python
# Rational arithmetic  
  
def add_rational(x, y):  
    """The sum of rational numbers X and Y."""  
    nx, dx = numer(x), denom(x)  
    ny, dy = numer(y), denom(y)  
    return rational(nx * dy + ny * dx, dx * dy)  
  
def mul_rational(x, y):  
    """The product of rational numbers X and Y."""  
    return rational(numer(x) * numer(y), denom(x) * denom(y))  
  
def rationals_are_equal(x, y):  
    """True iff rational numbers X and Y are equal."""  
    return numer(x) * denom(y) == numer(y) * denom(x)  
  
def print_rational(x):  
    """Print rational X."""  
    print(numer(x), "/", denom(x))  
```

## Pairs
```python
# unpacking
>>> pair = [1, 2]
>>> pair
[1, 2]
>>> x, y = pair
>>> x
1
>>> pair[0]
1

>>> from operator import getitem
>>> getitem(pair, 0)
1
```

### Representing Rational Numbers
```python
# Constructor and selectors  
  
def rational(n, d):  
    """A representation of the rational number N/D."""  
    return [n, d]  
  
def numer(x):  
    """Return the numerator of rational number X."""  
    return x[0]  
  
def denom(x):  
    """Return the denominator of rational number X."""  
    return x[1]
```

```python
# Improved specification  
  
from fractions import gcd  
def rational(n, d):  
    """A representation of the rational number N/D."""  
    g = gcd(n, d)  
    return [n//g, d//g] 
# reduction of fraction
```

## Abstraction Barriers
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205152031658.png)

### Violating Abstraction Barriers
```python
add_rational([1, 2], [1, 4])
# does not use constructors
def divide_rational(x, y):
	return [x[0] * y[1], x[1] * y[0]]
# no selectors! and no constructor
```

## Data Representations
```python
# Functional implementation  
  
def rational(n, d):  
    """A representation of the rational number N/D."""  
    g = gcd(n, d)  
    n, d = n//g, d//g  
    def select(name):  
        if name == 'n':  
            return n  
        elif name == 'd':  
            return d  
    return select  
  
def numer(x):  
    """Return the numerator of rational number X in lowest terms and having  
    the sign of X."""    return x('n')  
  
def denom(x):  
    """Return the denominator of rational number X in lowest terms and positive."""  
    return x('d')  
# selector calls the object itself
```

## Dictionaries
Associate keys and values

Dictionaries are **unordered** collections of key-value pairs
two restrictions:
+ A key of dictionary **cannot be** a list or a dictionary(or any *mutable type*)
+ Two **keys cannot be equal;** There can be at most one value for a given key
```python
# Dicts  
  
def dict_demos():  
    numerals = {'I': 1, 'V': 5, 'X': 10}  
    numerals['X']  
    numerals.values()  
    list(numerals.values())  
    sum(numerals.values())  
    dict([(3, 9), (4, 16), (5, 25)])  
    numerals.get('X', 0)
    # returns the value corresponding to 'X' or 0 
    numerals.get('X-ray', 0)  
    {x: x*x for x in range(3,6)}  
  
    {1: 2, 1: 3}  
    {[1]: 2}  
    {1: [2]}
```
## Examples: Lists
### Lists in Environment Diagrams
change the element after `append` doesn't matter
change the list after `extend` doesn't matter

addition & slicing may affect the original element since it's a copy

`pop`: removes & returns the last element
```python
s = [2, 3]
t = s.pop()
# t -> 3
```

`remove`: removes the first element equal to the argument