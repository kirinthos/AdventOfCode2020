#!/usr/local/bin/python3

import math
import re
from functools import partial, reduce
from itertools import combinations
from pprint import pprint

from common import drop, last, read_input, take_while_list, window

import numpy as np

data = [int(l) for l in read_input('data.input.day9')]

# do we care about processing? at least we'll use generators...
# walk a window of preamble + 1, the last being the one we check
def check(w):
    p = map(math.fsum, combinations(w[:-1], 2))
    v = w[-1]
    return any(map(lambda n: n == v, p))

preamble = 25
ans = next(x for x in drop(preamble, window(preamble + 1, data)) if not check(x))[-1]

# part 2
# find some set of at least 2 numbers that add to value from part 1
# i guess i still don't care about processing though...
def check_invalid(n, l):
    return math.fsum(l) <= n
p = partial(check_invalid, ans)
l = map(lambda v: drop(v, data), range(0, len(data) - 2))
solns = next(x for x in map(lambda v: last(take_while_list(p, v)), l) if math.fsum(x) == ans)
print(min(solns) + max(solns))
