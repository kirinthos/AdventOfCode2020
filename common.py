
from functools import reduce

def prod(l):
    return reduce(lambda a, n: a * n, l)

def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def partitionby(p, l):
    a = []
    for x in l:
        if p(x):
            a.append(x)
        else:
            yield a
            a = []

def flatten(l):
    return [item for sublist in l for item in sublist]

def count(l):
    return sum(1 for x in l)

def window(w, l):
    for i in range(0, len(l) - w):
        yield l[i:i+w]

def drop(n, l):
    for x in l:
        if n == 0:
            yield x
        else:
            n -= 1

def take_while_list(p, l):
    a = []
    for x in l:
        a.append(x)
        if p(a):
            yield a[:]
        else:
            return

def last(l):
    x = None
    for x in l:
        pass
    return x

def prime_factors(n):
    d = 2
    while n >= d:
        if n % d == 0:
            n /= d
            yield d
        else:
            d += 1

def read_input(name):
    return [l.strip() for l in open(name, 'r').readlines()]

