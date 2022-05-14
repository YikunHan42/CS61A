# Diagonostic Quiz
## Key Value Store
```python
def lens(prev = lambda x : 0):
	"""
	>>> put1 = lens()
	>>> get2, put2 = put1('cat', 'animal')
	>>> get3, put3 = put2('table', 'furniture')
	>>> get4, put4 = put3('cup', 'utensil')
	>>> get5, put5 = put4('thesis, 'paper')
	>>> get5('thesis')
	paper
	>>> get3('cup')
	0
	"""
	def put(k, v):
		def get(k2):
			if k2 == k:
				return v
			else:
				return prev(k2)
		return get, lens(get)
	return put
	"""
	def put(k, v):
		def get(k2):
			if k2 == k:
				return v
			else:
				return prev(k2)
		return get
	return put
	"""
```

## Storeroom
```python
def storeroom(helium, fn_even, fn_odd):
	"""
	>>> storeroom(1234, lambda x, y: x + y, lambda x, y: x * y)
	True
	4 + 2 > 3 * 1
	even > odd, from right to left
	"""
	evens_defined, odds_defined = False, False
	evens, odds = None, None
	while helium > 0:
		digit, helium = helium % 10, helium // 10
		if digits % 2 == 0:
			if not evens_defined:
				evens = digit
				evens_defined = True
			else:
				evens = fn_even(evens, digit)
		else:
			if not odds_defined:
				odds = digit
				odds_defined = True
			else:
				odds = fn_odd(odds, digit)
	return evens > odds
```

## Maximum Subnumber
```python
	def sculptural(ruler, k):
	"""
	>>> sculpture(32749, 2)
	79
	>>> sculptrue(32749, 18)
	32749
	"""
	if k == 0 or ruler == 0:
		return 0
	a = ruler % 10 + sculptural(ruler // 10, k - 1) * 10
	b = sculptural(ruler // 10, k)
	return max(a, b)
```

Base Case:
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205142136115.png)

Tree Recursion:
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205142139384.png)

Final:
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205142146540.png)
