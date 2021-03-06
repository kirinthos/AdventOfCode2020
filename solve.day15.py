#!/usr/local/bin/python3

import math
import re
from functools import partial, reduce
from itertools import combinations
from pprint import pprint

from collections import defaultdict

from common import read_input

import numpy as np

data = [list(map(int, l.split(','))) for l in read_input('data.input.day15')][0]

#data = [0,3,6]
#data = [1,3,2]
#data = [2,1,3]
#data = [1,2,3]
#data = [2,3,1]
#data = [3,1,2]

d = defaultdict(lambda: 0)
for i, v in enumerate(data[:-1]):
    d[v] = i + 1

def process(d, acc, n):
    vs = d[acc]
    l = n - 1
    if vs > 0:
        v = l - vs
    else:
        v = 0
    d[acc] = l
    return v

# yeah closures, but also FP
f = partial(process, d)
print(reduce(f, range(len(data) + 1, 30000000 + 1), data[-1]))
