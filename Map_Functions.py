# Syntax = map(fun, iter)

def double(n):
    return n * 2

n = [5, 6, 7, 8]
res = map(double, n)
print(list(res))