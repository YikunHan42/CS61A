# Tree Recursion
[[CS61A]]
![[07-Tree_Recursion_1pp.pdf]]

## Tree Strcture
**fib(n)**: 0, 1, 1, 2, 3, 5, 8, 13, 21

```python
"""
from ucb import trace

@trace
"""
def fib(n):
	if n == 0: return 0
	elif n == 1: return 1
	else: return fib(n - 2) + fib(n - 1) # so slow
```

### Repetition in Tree-Recursive Computation
highly repetitive; `fib` is called on the same argument multiple times.

## Paths
Total number of ways to get to $(M,N)$= Total number of ways to get to $(M - 1,N)$+otal number of ways to get to $(M,N + 1)$
```python
def paths(m, n):
	"""Return the number of paths from one corner of an N by N grid to the opposite corner.

	>>> paths(2, 2)
	2
	>>> paths(5, 7)
	210
	>>> paths(117, 1)
	1
	>>> paths(1, 157)
	1
	"""
	if(m == 1 or n == 1): return 1
	else: return paths(m - 1, n)+ paths(m, n - 1)
```

## Knapsack
```python
def knap(n, k):
	"""Return if number of n can add up to k.

	>>> knap(689, 15)
	True
	>>> knap(689, 16)
	False
	"""
	if n == 0: return k == 0
	with_last = knap(n // 10, k - n % 10)
	without_last = knap(n // 10, k)
	return with_last or without_last
```

## Counting Partitions
`count_partitions(6, 4)
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205121118957.png)

Explore two possibilities:
+ Use at least one 4
+ Don't use any 4

Solve two simpler problems:
+ `count_partitions(2, 4)`
+ `count_partitions(6, 3)`

```python
def count_partitions(n, m):
	if n == 0:
		return 1
	if n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		with_m = count_partitions(n - m, m)
		without_m = count_partitions(n, m - 1)
		return with_m + without_m
```

## Binary Print
```python
def all_nums(k):
	def h(k, prefix):
		if k == 0:
			print(prefix)
			return 0
		h(k - 1, prefix * 10)
		h(k - 1, prefix * 10 + 1)
	h(k, 0)
```

$prefix$ actually varies, take `all_nums(4)` as an example, $0 \leq prefix \leq 111$, specially when it's a four digit number, $100 \leq prefix \leq 111$
The inverse print order allows to represent the number in an ascending sequence

## Implementing Functions
```python
def remove(n, digit)
	"""Return all digits of non-negative N that are not DIGIT, for some non-negative DIGIT less than 10. 
	>>> remove(231, 3)
	21
	>>> remove(243132, 2)
	4313
	"""
	kept, digits = 0, 0
	while n > 0:
		n, last = n // 10, n % 10
		if last != digit:
			kept = kept + last * 10 ** digits
			digits = digits + 1
	return kept 
```