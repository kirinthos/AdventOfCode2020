#!/usr/local/bin/python3

import math
import re
from collections import defaultdict
from functools import partial, reduce
from pprint import pprint

from common import flatten, read_input

import numpy as np

data = [l.split(' = ') for l in read_input('data.input.day14')]

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def mask_pairs(mask_str):
    return [(i, c == '1') for i, c in enumerate(reversed(mask_str)) if c != 'X']

def mask_value(mask, value):
    for i, m in mask:
        if m:
            value = set_bit(value, i)
        else:
            value = clear_bit(value, i)
    return value



def run(data):
    mem = defaultdict(lambda: 0)
    for l in data:
        cmd, val = l
        if cmd == 'mask':
            pairs = mask_pairs(val)
            f = partial(mask_value, pairs)
        elif cmd.startswith('mem'):
            addr = int(cmd[4:-1])
            mem[addr] = f(int(val))
    return mem

#print(sum(run(data).values()))

# part 2
# overwrites part 1 functions

def mask_pairs(mask_str):
    return [(i, c) for i, c in enumerate(reversed(mask_str))]

def mask_value(mask, value):
    values = [value]
    for i, m in mask:
        if m == '1':
            values = list(map(lambda v: set_bit(v, i), values))
        elif m == 'X':
            values = flatten([(set_bit(v, i), clear_bit(v, i)) for v in values])
    return values

def run(data):
    mem = defaultdict(lambda: 0)
    for l in data:
        cmd, val = l
        if cmd == 'mask':
            pairs = mask_pairs(val)
            f = partial(mask_value, pairs)
        elif cmd.startswith('mem'):
            addrs = f(int(cmd[4:-1]))
            for a in addrs:
                mem[a] = int(val)
    return mem

print(sum(run(data).values()))
