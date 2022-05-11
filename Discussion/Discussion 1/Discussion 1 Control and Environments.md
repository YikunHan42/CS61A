# Control and Environments
![[disc01.pdf]]

[[CS61A]]
## Control
### If statements
truthy values(True, a non-zero integer, etc.), falsy values(False, 0, None, "", [], etc.): 

### Boolean Operators
+ `and` : If all values evaluated to a true value, the last value is returned
+ `or` : If all values evaluated to a false value, the last value is returned

#### Questions
```python
def wears_jacket_with_if(temp, raining):  
    """  
    >>> wears_jacket_with_if(90, False)  
    False    >>> wears_jacket_with_if(40, False)  
    True    >>> wears_jacket_with_if(100, True)  
    True    """    if temp < 60 or raining == True: return True  
    else: return False  
  
def wears_jacket(temp, raining):  
    return True if temp < 60 or raining == True else False
```

### While loops
#### Questions
```python
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
    False    >>> is_prime(7)  
    True    """    i = 2  
    while i <= sqrt(n):  
        if(n % i == 0) : return False  
        i += 1  
    return True
```

## Environment Diagrams
### Call Expressions
Procedure:
1. Evaluate the operator, which should evaluate to a function.
2. Evaluate the operands from left to right.
3. Draw a new frame, labelling it with the following:
	+ A unique index(f1, f2, f3, ...)
	+ The **intrinsic name** of the function, which is the name of the function object iteself. For example, if the function object is `func square(x)[parent=Global]`, the intrinsic value is square.
	+ The parent frame([parent=Global])
4. Bind the formal parameters to the argument values obtained in step 2(e.g. bind $x$ to  3).
5. Evaluate the body of the function in this new frame until a return value is obtained. Write down the return value in the frame.

 no return value -> returns $None$

#### Proceed with call-tion
```python
x = 3

def p(rint):
	print(rint)

def g(x,y):
	if x:
		print("one")
	elif x:
		print(True, x)
	if y:
		print(True, y)
	else:
		print(False, y)
	return print(p(y)) + x
```

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205031527178.png)

Explanation:

x, y = 2, x
`g(y, x)`:
Here y = 3 , x = 2
1. `if 3`
2. `if 2`
3. `print(2)`
4. `print(None)`
5. `return None + 3`

`g(y, p("rint"))`:
1. `p("rint")`
2. `if 3`
3. `else: print(False) print(None)`
4. `print(None)`
5. `print(None)`
6. `return None + 3`