
from functools import reduce

def prod(l):
    return reduce(lambda a, n: a * n, l)

def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def flatten(l):
    return [item for sublist in l for item in sublist]

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

def read_input(name):
    return [l.strip() for l in open(name, 'r').readlines()]

