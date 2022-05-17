# Functional Decomposition & Debugging
[[CS61A]]
![[09-Functional_Decomposition_&_Debugging_1pp.pdf]]

## Assert
```python
def fact(x):
	assert isinstance(x, int)
	assert x >= 0
	if x == 0:
		return 1
	else:
		return x * fact(x - 1)
def half_fact(x):
	return fact(x / 2)
```

Code should fail as sson as possible -> makes error detection easier

Limitations:
+ require invariants
+ check that code meets an existing understanding

### Demo
```python
# Taylor
def t(f, n, x, x0 = 0):

	r = 0
	while n:
		r += (x - x0) ** n / fact(n) * d(n, f)(x0)
		n -= 1
	return r
```

## Testing
+ Detect errors in your code
+ *Have confidence* in the correctness of subcomponents
+ *Narrow down* the scope of debugging
+ *Document* how your code works

### Doctests
provides a a way to write tests as part of the docstring

#### Limitations
do not treat `print` and `return` differently

## Print Debugging
### ok integration
based on doctest
`print("debug=...")`

## Interactive Debugging
don't want to run the code every time

### REPL
`python ok -q whatever -i`

### PythonTutor
[PythonTutor](tutor.cs61a.org)
`python ok -q whatever --trace`

## Error Types
### Message Patterns
+ not necessary
+ messy
+ not universal laws of nature
	+ are true >90% of the time

### Syntax Error
The file you ran isn't valid python syntax

### Indentation Error
The file you ran isn't valid python syntax, because of indentation inconsisitency

**More than one kind of space**

### TypeError
#### 'X' object is not callable
Objects of type X cannot be treated as functions
higherorderfunction: 
`g(h)` but you pass in `g(2)`

#### TypeError: ... NoneType ...
You use None in some operation it wasn't meant for

### NameError or UnboundLocalError
Python looked up a name but didn't find it

## Traceback
```python
def f(x):
	1 / 0
def g(x):
	f(x)
def h(x):
	g(x)
print(h(2))
```

**Most recent call is at the bottom**, not always the last one calls the error

## Exceptions
### Handling Errors
Sometimes, computer programs behave in non-standard ways

### Exceptions
A built-in mechanism in a programming language to declare and respond to exceptional conditions
Python *raises* an exception whenever an error occurs

**Mastering exceptions**:
Exceptions are objects: They have classes with constructors
They enable *non-local* continuations of control: If `f` calls `g` and `g` calls `h`, exceptions can shift control from `h` to `f` without waiting for `g` to return
(Exception handling tends to be slow)

## Raising Exceptions
### Assert Statements
raise an exceptin of type AssertionError
`assert <expression>, <string>`
if the expression is False, print string
`python -0` without assertion

### Raise Statemets
`raise <expression>`
expression must evaluate to a subclass of BaseException or an instance of one
raise + some kinds of error
`raise TypeError('Bad argument')`

## Try Statements
```python
try:
	<try suite>
except <exception class> as <name>:
	<except suite>
```

If the class of the exception inherits from exception class, then except suite is executed

### Handling Exceptions
```python
try:
	x = 1 / 0
except ZeroDivisionError as e:
	print('handling a', type(e))
	x = 0
```

mutiple try statements: control jumps to the expect suite of the most recent try statement

```python
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
```

### WWPD
```python
def invert(x):
	result = 1 / x
	print('Never printed if x is 0')
	return result

def invert_safe(x):
	try:
		return invert(x)
	except ZeroDivisionError as e:
		return str(e)
```

## Reduce
```python
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
```