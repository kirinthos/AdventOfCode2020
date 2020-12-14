#!/usr/local/bin/python3

import math
import re
from functools import partial, reduce
from pprint import pprint

from common import prod, read_input

import numpy as np

data = read_input('data.input.day13')
time = int(data[0])
buses = [int(d) for d in data[1].split(',') if d != 'x']

routes = [(time // v + 1) * v for v in buses]
m = min(routes)
b = buses[routes.index(m)]
#print((m - time) * b)

# part 2
buses_ts = [(int(d), i) for i, d in enumerate(data[1].split(',')) if d != 'x']

"""
# a failed attempt. i ended up finding the solution from defining this one!

# adjust time frames into "max value" to yield least cycles
buses_ts.sort(key=lambda v: v[0], reverse=True)
base, adj = buses_ts.pop(0)
buses_ts = [(d, v - adj) for d, v in buses_ts]

t = base
while True:
    #print(t)
    if all(map(lambda v: ((t + v[1]) % v[0]) == 0, buses_ts)):
        break
    t += base

print(t - adj)
"""

# so i noticed that we created a sequence of congruence classes in the above
# solution. so i googled for solving system of congruence classes and found
# that this is the Chinese Remainder Theorem!
# we can solve this using inverse modular values, for which we need euclidian extension

# doing this here, to note that i didn't swap before, put it in `a (mod n)` form
# we also have to "rotate the ring", by subtracting the number of minutes from the ID
# because being 1 minute after the timestamp is being (n - 1) minutes before the next bus arrival
buses_ts_mod = list(map(lambda v: ((v[0] - v[1]) % v[0], v[0]), buses_ts))

def invmod(a, n):
    """Extended Euclid, from wikipedia"""
    old_r, r = a, n
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # sign might not be correct, but always positive for this problem
    # operating within a ring, we can't just reverse sign, we have to go
    # 'around the ring' by adding the modulus
    if old_s < 0:
        old_s += n
    return old_s

def congruence_system(system):
    """Chinese remainder theorem, constructionist expansion"""
    N = prod(v[1] for v in system)
    return sum(a * N // n * invmod(N // n, n) for a, n in system) % N

c = congruence_system(buses_ts_mod)
print(c)
