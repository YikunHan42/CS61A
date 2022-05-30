# Tree Recursion & Lists
![[disc04.pdf]]
[[CS61A]]

## Recursion
recursive definition
1. figure out base case
2. make a recursive call with a simpler argument
3. use recursive call to solve the full problem

### Questions
1.1 Write a function that takes two numbers m and n and returns their product.
Assume m and n are positive integers. Use recursion, not mul or *!
Hint: 5*3 = 5 + 5*2 = 5 + 5 + 5*1.
For the base case, what is the simplest possible input for multiply?
For the recursive case, what does calling multiply(m - 1, n) do? What does calling multiply(m, n - 1) do? Do we prefer one over the other?

```python
def multiply(m, n):
	"""
	>>> multiply(5, 3)
	15
	"""
	if n == 1: return m
	else: return m + multiply(m, n - 1)
```

1.2 Below is the iterative version of is prime, which returns True if positive integer n is a prime number and False otherwise:

```python
def is_prime(n):
	"""
	>>> is_prime(7)
	True
	>>> is_prime(10)
	False
	>>> is_prime(1)
	False
	"""
	if n == 1:
		return False
	k = 2
	while k < n:
		if n % k == 0:
			return False
		k += 1
	return True
```

Implement the recursive is prime function. Do not use a while loop, use recursion. As a reminder, an integer is considered prime if it has exactly two unique factors: 1 and itself.
```python
def is_prime(n):
	if n == 1 or n == 0:
		return False
	return is_prime(n, 2)
	
def prime_helper(n, m)
	if m == n - 1:
		return True
	elif n % m == 0:
		return False
	else:
		return prime_helper(n, m + 1)
```

## Tree Recursion
try multiple possibilities at the same time

### Questions
2.1 You want to go up a ﬂight of stairs that has n steps. You can either take 1 or 2 steps each time. How many diﬀerent ways can you go up this ﬂight of stairs? Write a function count_stair_ways that solves this problem. Assume n is positive.
Before we start, what’s the base case for this question? What is the simplest input?
What do count_stair_ways(n - 1) and count_stair_ways(n - 2) represent?
Fill in the code for count stair ways:

```python
def count_stair_ways(n):
	if n == 0: return 0
	elif n == 1: return 1
	elif n == 2: return 2
	return count_stair_ways(n - 1) + count_stair_ways(n - 2)
```

2.2 Consider a special version of the count_stairways problem, where instead of taking 1 or 2 steps, we are able to take up to and including k steps at a time.
Write a function count_k that ﬁgures out the number of paths for this sce-nario. Assume n and k are positive.

```python
def count_k(n, k):
	"""
	>>> count_k(3, 3)
	4
	>>> count_k(4, 4)
	8
	>>> count_k(10, 3)
	274
	>>> count_k(300, 1)
	1
	"""
   if n == 0: return 1  
   elif n < k: return count_k(n, n)  
   else:  
      sum = 0  
      for i in range(1, k + 1, 1):  
         sum += count_k(n - i, k)  
      return sum
```

## Lists
A *sequence* is an ordered collection of value

### List Slicing
### List Comprehensions
`[x * x - 3 for x in [1, 2, 3, 4, 5] if x % 2 == 1]`
result in the ouput of [-2, 6, 22]

### Questions
3.1 What would Python display?
```python
"""
>>> a = [1, 5, 4, [2, 3], 3] 
>>> print(a[0], a[-1])
1 3
>>> len(a)
5
>>> 2 in a
False
>>> 4 in a
True
>>> a[3][0]
2
"""
```

3.2 Write a function that takes a list s and returns a new list that keeps only the even-indexed elements of s and multiplies them by their corresponding index.
```python
def even_weighted(s):
	"""
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
	[0, 6, 20]
	"""
	return [s[i] * i for i in range(len(s)) if i % 2 == 0]
```

3.3 Write a function that takes in a list and returns the maximum product that can be formed using nonconsecutive elements of the list. The input list will contain only numbers greater than or equal to 1.
```python
def max_product(s):
	"""Return the maximum product that can be formed using non-consective elements of s.
	>>> max_product([10, 3, 1, 9, 2])
	90
	>>> max_product([5, 10, 5, 10, 5])
	125
	>>> max_product([])
	1
	"""
	n = len(s)
    def prod(i, odevity):
        if i >= n:
            return 1
        elif odevity == 'odd':
            return prod(i + 1, 'even')
        else:
            return max(prod(i + 1, 'odd') * s[i], prod(i + 1, 'even'))
        # even now, no consecutive elements are allowed
	return prod(0, 'even')
```



1. Whole Numbers

   (a) A hole number is a number in which every other digit dips below the digits immediately adjacent to it. For example, the number 968 would be considered a hole number because the number 6 is smaller than both of its surrounding digits. Assume that we only pass in numbers that have an odd number of digits. Define the following function so that it properly identifies hole numbers.

   ```python
   def check_hole_number(n):
       """
       >>> check_hole_number(123)
       False
       >>> check_hole_number(3241968)
       True
       >>> check_hole_number(3245968)
       False
   
       968 419 324
       """
       if n // 10 == 0:
           return True
       return n // 10 % 10 < n % 10 and n // 10 % 10 < n // 100 % 10 and check_hole_number(n // 100)
   ```

​		

​		(b) Define the following function so that it properly identifies mountain numbers. A mountain number is a number that either

​		i.	has digits that strictly decrease from right to left OR strictly increase from right to left
​		ii.	has digits that increase from right to left up to some point in the middle of the number (not necessarily the exact middle digit). After reaching the maximum digit, the digits to the left of the maximum digit should strictly decrease.

