#!/usr/local/bin/python3

import math
from functools import reduce
from itertools import groupby
from pprint import pprint

from common import read_input

import numpy as np

data = read_input('data.input.day6')

# we have to build groups, then people, so lets reduce
def group(acc, n):
    if n == '':
        acc.append([])
    else:
        acc[-1].append(set(n)) # changed to sets for part 2
    return acc
groups = reduce(group, data, [[]])

#print(sum(map(lambda v: len(set(''.join(v))), groups)))

# part 2
# cardinality of intersection of sets of answers
print(sum(map(lambda g: len(reduce(lambda acc, n: acc.intersection(n), g)), groups)))
