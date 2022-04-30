# Functions
[[CS61A]]

![[02-Functions_full.pdf]]

## Names, Assignment, and User-Defined Functions
```python
# Imports  
from math import pi  
pi * 71 / 223  
from math import sin  
sin(pi/2)  
  
# Assignment  
radius = 10  
2 * radius  
area, circ = pi * radius * radius, 2 * pi * radius  
radius = 20 # don't remember 
  
# Function values  
max  
max(3, 4)  
f = max  
f  
f(3, 4)  
max = 7  
f(3, 4)  
f(3, max) # bound and rebound 
f = 2  
# f(3, 4)  
__builtins__.max  
  
# User-defined functions  
from operator import add, mul  
  
def square(x):  
    return mul(x, x)  
  
square(21)  
square(add(2, 5))  
square(square(3))  
  
def sum_squares(x, y):  
    return add(square(x), square(y))  
sum_squares(3, 4) # call user-defined functions  
sum_squares(5, 12)  
  
# area function  
def area():  
    return pi * radius * radius  
area()  
radius = 20  
area()  
radius = 10  
area() # function rather than variable
  
# Name conflicts  
def square(square):  
    return mul(square, square)  
square(4)
```

## Environment Diagrams
### Codes & Frames
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301704482.png)

### Assignment Statements
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301706077.png)
**Evaluate all then Bind all**

### Discussion Q1 Solution
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301709327.png)

## Defining Functions
Function definition is a more powerful means of abstractions: bind names to **expressions**

* Function *signature* indicates how many arguments a functiontakes
* Function *body* defines thecomputational process expressed by a function 

Execution procedure:
1. Create a function with signature `<name>(<formal parameters>`
2. Set the body of that function to be everything indented after the first line
3. Bind `<name>` to that function in the current frame

`def` do not execute until the function is called

### Calling User-Defined Functions
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301718051.png)

A function's *signature* has all the information needed to create a local frame

### Looking Up Names in Environments
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301723589.png)

Order is important(First local frame, then global frame)
```python
from operator import mul
mul(3, 4)

def square(square):
	return mul(square, square)

square(-2) # still works
```

Since
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301726876.png)
