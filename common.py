
from functools import reduce

def prod(l):
    return reduce(lambda a, n: a * n, l)

def read_input(name):
    return [l.strip() for l in open(name, 'r').readlines()]
