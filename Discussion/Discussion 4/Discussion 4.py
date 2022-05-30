def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
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

def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper():
        if:
            return
        if:
            return
        return
    return helper()


