
import math
from functools import reduce

def prod(l):
    return reduce(lambda a, n: a * n, l)

def add(l1, l2):
    return map(sum, zip(l1, l2))

def negate(l):
    return map(lambda v: v * -1, l)

def sub(l1, l2):
    return map(sum, zip(l1, negate(l2)))

def product(l1, l2):
    return map(prod, zip(l1, l2))

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

def rotate_around_pt(center, pt, deg):
    center = list(center)
    pt = list(pt)
    r = math.pi * deg / 180.0
    c, s = math.cos(r), math.sin(r)
    x, y = pt[0] - center[0], pt[1] - center[1]
    return center[0] + c * x - s * y, center[1] + s * x + c * y


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

