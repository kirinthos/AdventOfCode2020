#!/usr/local/bin/python3

import math

from functools import reduce
from itertools import combinations

with open('data.input', 'r') as f:
    data = [int(l.strip()) for l in f.readlines()]

pair = next(v for v in combinations(data, 2) if v[0] + v[1] == 2020)
#print(pair[0] * pair[1])

# part 2
trip = next(v for v in combinations(data, 3) if math.fsum(v) == 2020)
# no math.prod?
def prod(l):
    return reduce(lambda a, n: a * n, l)
print(prod(trip))
