# Higer-Order Functions
[[CS61A]]
![[04-Higher-Order_Functions_1pp.pdf]]

## Generalizing Patterns with Arguments
**Finding common structures for shared implementation**

`assert` statement

```python
# Generalizing patterns using arguments

from math import pi, sqrt

def area_square(r):
    """Return the area of a square with side length R."""
    return r * r

def area_circle(r):
    """Return the area of a circle with radius R."""
    return r * r * pi

def area_hexagon(r):
    """Return the area of a regular hexagon with side length R."""
    return r * r * 3 * sqrt(3) / 2

def area(r, shape_constant):
    """Return the area of a shape from length measurement R."""
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)
```

## Generalizing Over Computational Processes
```python
# Functions as arguments

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

from operator import mul

def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

summation(1000000, pi_term)

```

## Functions as Return Values
```python
# Local function definitions; returning functions

def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> add_three = make_adder(3) # k is 3
    >>> add_three(4) # n is 4
    7
    """
    def adder(k):
        return k + n # return a value
    return adder # return a function

make_adder(2000)(19)

```

### Locally Defined Functions
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205030220866.png)

### Call Expressions as Operator Expressions
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205030222757.png)

### The Purpose of Higher-Order Functions
Definition: A function that **takes a function as an argument value or returns a function as a return value**

Benefits:
+ Express general methods of computation
+ Remove repetition from programs
+ separate concerns among functions

## Function Example: Sounds
The Waveform Audio File Format encodes a sampled sound wave

Triangle Wave:
Mario song:
```python
# Example: Sound

from wave import open
from struct import Struct
from math import floor

frame_rate = 11025 # How high or low

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.html)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
    """Write the output of a sampler function as a wav file.
    (See https://docs.python.org/3/library/wave.html)
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()

def tri(frequency, amplitude=0.3):
    """A continuous triangle wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

play(tri(e_freq))

def note(f, start, end, fade=.01): # fade in and out 
    """Play f for a fixed duration."""
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

play(note(tri(e_freq), 1, 1.5))

def both(f, g):
    return lambda t: f(t) + g(t)

c = tri(c_freq)
e = tri(e_freq)
g = tri(g_freq)
low_g = tri(g_freq / 2)

play(both(note(e, 0, 1/8), note(low_g, 1/8, 3/8)))

play(both(note(c, 0, 1), both(note(e, 0, 1), note(g, 0, 1))))

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))
    return song

def mario_at(octave):
    c = tri(octave * c_freq)
    e = tri(octave * e_freq)
    g = tri(octave * g_freq)
    low_g = tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)

play(both(mario_at(1), mario_at(1/2)))
```
1. Delay execution → sharing a dropbox file as a callback
2. Break down latency → take advantage of python decorater

## Function Compositioon
```python

# Composition

def compose1(f, g): # composite function / hybrid function
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x): # You can't simply return f(g)
        return f(g(x))
    return h # define a number and extract the function

def triple(x):
    return 3 * x

squiple = compose1(square, triple)
tripare = compose1(triple, square)
squadder = compose1(square, make_adder(2))
```

`compose1(sqaure, make_adder(2))(3)`
first $g(3)$ = 2+3 = 5
then return 25

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205031348666.png)

## Function Currying
adding
```python
def make_adder(n):
	return lambda k: n + k
```

```python


# Currying

from operator import add, mul

def curry2(f):
    """Curry a two-argument function.

    >>> m = curry2(add)
    >>> add_three = m(3) # x= 3
    >>> add_three(4) # y = 4
    7
    >>> m(2)(1)
    3
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
# h returns f, g returns h, f returns g
# curry2 = lambda f: lambda x: lambda y: f(x, y)
```

## Abstraction
### Choosing Nmaes
matter a lot for composition

+ Names should convey the *meaning* or *purpose* of the values to which they are bound
+ The type of value bound to the name is best documented in a function's doctstring 
+ Function names typically convey their effect(print), their behavior(triple), or the value returned(abs)
+ Names can be long if they help document your code
+ Names can be short if they represent generic quantities: counts, arbitrary functions, arguments to mathematical operations, etc.

### Which Values Deserve a Name
+ *Repeated compound expressions*
+ *Meaningful parts of complex expressions*

## Code









