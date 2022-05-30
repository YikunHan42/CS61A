# Trees
[[CS61A]]

![[10-Trees_1pp.pdf]]

## Box-and-Pointer Notation
<center>Lists: a wrow of index-label adjacent boxes</center>
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205301607889.png)

## Slicing
```python
# Slicing  
  
odds = [3, 5, 7, 9, 11]  
list(range(1, 3))  
[odds[i] for i in range(1, 3)]  
odds[1:3] # [5, 7]  
odds[1:]  
odds[:3] # get a new list rather than changing the original one 
odds[:] 
```

## Processing Container Values
built-in functions take iterable arguments and aggregate them into a value
```python
sum([2, 3, 4])
sum(['2', '3', '4']) # error

sum([2, 3, 4], 5)

max(range(5))
max(0, 1, 2, 3, 4)

max(range(10), key = lambda x: 7 - (x - 4) * (x - 2))
# returns 3
(lambda x: 7 - (x - 4) * (x - 2))(3)
# returns the maximum value

all([x < 5 for x in range(5)])
# all true

# Aggregation  
  
sum(odds)  
sum({3:9, 5:25})  
max(range(10))  
max(range(10), key=lambda x: 7 - (x-2)*(x-4))  
all([x < 5 for x in range(5)])  
perfect_square = lambda x: x == round(x ** 0.5) ** 2  
any([perfect_square(x) for x in range(50, 60)]) # Try ,65)
```

## Trees
### Common Vocabularies
#### Recursive description
+ A tree has a root label and a list of branches
+ Each branch is a tree
+ A tree with zero branches is called a **leaf**

#### Relative description
Each location in a tree is called a node
Each node has a label that can be any value
One node can be the parent/child of another

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205301619245.png)

### Implemeting the Tree Abstraction
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202205301621191.png)

```python
# Trees  
  
def tree(label, branches=[]):  
    for branch in branches:  
        assert is_tree(branch), 'branches must be trees'  
    return [label] + list(branches)  
  
def label(tree):  
    return tree[0]  
  
def branches(tree):  
    return tree[1:]  
  
def is_tree(tree):  
    if type(tree) != list or len(tree) < 1:  
        return False  
    for branch in branches(tree):  
        if not is_tree(branch):  
            return False  
    return True  
def is_leaf(tree):  
    return not branches(tree)
```

## Tree Processing
```python
### +++ === ABSTRACTION BARRIER === +++ ###  
  
def fib_tree(n):  
    """Construct a Fibonacci tree.  
  
    >>> fib_tree(1)    [1]    >>> fib_tree(3)    [2, [1], [1, [0], [1]]]    >>> fib_tree(5)    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]    """    if n == 0 or n == 1:  
        return tree(n)  
    else:  
        left = fib_tree(n-2)  
        right = fib_tree(n-1)  
        fib_n = label(left) + label(right)  
        return tree(fib_n, [left, right])  
        # return tree(label(left) + label(right), [left, right])
```

### Tree Processing Uses Recursion
```python
def count_leaves(t):  
    """The number of leaves in tree.  
  
    >>> count_leaves(fib_tree(5))    8    """    if is_leaf(t):  
        return 1  
    else:  
        return sum([count_leaves(b) for b in branches(t)]) 
```

```python
def leaves(tree):  
    """Return a list containing the leaf labels of tree.  
  
    >>> leaves(fib_tree(5))    [1, 0, 1, 0, 1, 1, 0, 1]    """    if is_leaf(tree):  
        return [label(tree)]  
    else:  
        return sum([leaves(b) for b in branches(tree)], [])
```

```python
def increment_leaves(t):  
    """Return a tree like t but with leaf labels incremented.  
          
    >>> print_tree(increment_leaves(fib_tree(4)))  
    3      1        1        2      2        2        1          1          2    """    if is_leaf(t):  
        return tree(label(t) + 1)  
    else:  
        bs = [increment_leaves(b) for b in branches(t)]  
        return tree(label(t), bs)  
  
def increment(t):  
    """Return a tree like t but with all labels incremented.  
        >>> print_tree(increment(fib_tree(4)))  
    4      2        1        2      3        2        2          1          2    """    return tree(label(t) + 1, [increment(b) for b in branches(t)])
```

## Printing Trees
```python
def print_tree(t, indent=0):  
    """Print a representation of this tree in which each label is  
    indented by two spaces times its depth from the root.  
    >>> print_tree(tree(1))    1    >>> print_tree(tree(1, [tree(2)]))    1      2    >>> print_tree(fib_tree(4))    3      1        0        1      2        1        1          0          1    """    print('  ' * indent + str(label(t)))  
    for b in branches(t):  
        print_tree(b, indent + 1)
```