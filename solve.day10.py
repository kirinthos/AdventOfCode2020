#!/usr/local/bin/python3

import math
import re
from functools import partial, reduce
from itertools import combinations
from pprint import pprint

from common import drop, partitionby, prod, read_input

import numpy as np

data = [int(l) for l in read_input('data.input.day10')]
data = [0] + data + [max(data) + 3]
data = np.sort(np.array(data))

diffs = data[1:] - data[:-1]
#print(sum(diffs == 1) * sum(diffs == 3))

# part 2

f = lambda v: v == 1
ld = list(map(len, partitionby(f, diffs)))

# okay, so i use a diff map which has 1 less member per group of adapters, that's why we have "- 1"
# instead of "- 2", for each set of adapters we have the varying sequences we can turn on/off

# [(0, 1, 2, 3, 4), (0, 1, 2, 4), (0, 1, 4), (0, 1, 3, 4), (0, 3, 4), (0, 2, 3, 4)]
# notice there are (length - 2) * 2 choices.
# but then also the additional case: (0, 2, 4) and this occurs once for every 5 numbers, but every 4 diffs!

l = [(v - 1) * 2 + v // 4 for v in ld if v > 1]

print(prod(l))
