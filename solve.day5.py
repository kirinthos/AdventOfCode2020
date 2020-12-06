#!/usr/local/bin/python3

import math
from functools import reduce
from pprint import pprint

from common import read_input

import numpy as np

data = read_input('data.input.day5')


# we'll start with a range, and then bisect it recursively
def bisect(acc, n):
    r = math.ceil((acc[1] - acc[0]) / 2)
    return (acc[0], acc[1] - r) if n in ('F', 'L') else (acc[0] + r, acc[1])

rows = np.array(list(map(lambda v: reduce(bisect, v[:7], (0, 127))[0] * 8, data)))
cols = np.array(list(map(lambda v: reduce(bisect, v[7:], (0, 7))[0], data)))

ids = np.sort(rows + cols)
#print(ids.max())

# part 2
l = len(ids)
print(np.where((ids[1:] - ids[:l-1]) == 2)[0] + 1 + ids[0])
