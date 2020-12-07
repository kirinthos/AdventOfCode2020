
from functools import reduce

def prod(l):
    return reduce(lambda a, n: a * n, l)

def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def flatten(l):
    return [item for sublist in l for item in sublist]

def read_input(name):
    return [l.strip() for l in open(name, 'r').readlines()]

