# Syntax = map(fun, iter)

def double(n):
    return n * 2

n = [5, 6, 7, 8]
res = map(double, n)
print(list(res))


# Reduce  function
import functools

n = [1, 2, 3, 4]

prod = functools.reduce(lambda x, y: x * y, n)
print(prod)

# Filter Function

def is_even(n):
    return n % 2 == 0

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

en = filter(is_even, n)
print(list(en))

# Combined Examples
from functools import reduce

n = [1, 2, 3, 4, 5, 6]

e = filter(lambda x: x % 2 == 0, n)
s = map(lambda x: x**2, e)
res = reduce(lambda x, y: x + y, s)

print(res)