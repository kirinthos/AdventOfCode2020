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

d = defaultdict(lambda: [])
for i, v in enumerate(data[:-1]):
    d[v] = [i + 1]

def process(d, acc, n):
    vs = d[acc]
    if len(vs) > 0:
        v = n - 1 - vs[-1]
    else:
        v = 0
    vs.append(n - 1)
    return v

# yeah closures, but also FP
f = partial(process, d)
print(reduce(f, range(len(data) + 1, 30000000 + 1), data[-1]))
