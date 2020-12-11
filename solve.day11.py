#!/usr/local/bin/python3

import math
import re
from functools import partial, reduce
from itertools import product
from pprint import pprint

from common import flatten, read_input

import numpy as np

data = read_input('data.input.day11')


def translate(c):
    if c == '.':
        return None
    return c == '#'

def untranslate(c):
    if c is None:
        return '.'
    return '#' if c == True else 'L'

data = [list(map(translate, sub)) for sub in data]

def nonesum(l):
    return sum(map(lambda v: 0 if v is None else v, l))

def kernel(grid, dirs, x, y):
    xl = len(grid[0])
    yl = len(grid)
    def check(v):
        return v[0] >= 0 and v[1] >= 0 and v[0] < yl and v[1] < xl
    pts = map(lambda v: grid[v[0]][v[1]], filter(check, map(lambda d: (y + d[0], x + d[1]), dirs)))
    return nonesum(pts)

def cycle(grid):
    ds = [0, 1, -1]
    dirs = list(product(ds, ds))
    dirs.remove((0, 0))
    yl = len(grid)
    xl = len(grid[0])
    ng = [g[:] for g in grid]

    for y in range(yl):
        for x in range(xl):
            if grid[y][x] == True and kernel(grid, dirs, x, y) >= 4:
                ng[y][x] = False
            elif grid[y][x] == False and kernel(grid, dirs, x, y) == 0:
                ng[y][x] = True
    return ng

def printgrid(grid):
    ng = [''.join(map(lambda v: untranslate(v), g)) for g in grid]
    pprint(ng)

#pg = None
#while data != pg:
    #pg = data
    #data = cycle(data)


#print(nonesum(flatten(data)))

# part 2
# instead of kernels, we're now going to shoot rays out in each direction

def inrange(grid, pt):
    return pt[0] >= 0 and pt[1] >= 0 and pt[0] < len(grid[0]) and pt[1] < len(grid)

def ray(grid, d, x, y):
    pt = (x + d[0], y + d[1])
    while inrange(grid, pt) and grid[pt[1]][pt[0]] is None:
        pt = (pt[0] + d[0], pt[1] + d[1])
    return pt if inrange(grid, pt) else None

def cycle2(grid):
    ds = [0, 1, -1]
    dirs = list(product(ds, ds))
    dirs.remove((0, 0))
    yl = len(grid)
    xl = len(grid[0])
    ng = [g[:] for g in grid]

    for y in range(yl):
        for x in range(xl):
            v = grid[y][x]
            if v is None:
                continue

            pts = filter(lambda v: v is not None, [ray(grid, d, x, y) for d in dirs])
            elems = [grid[p[1]][p[0]] for p in pts]
            if v == True and nonesum(elems) >= 5:
                ng[y][x] = False
            elif v == False and nonesum(elems) == 0:
                ng[y][x] = True
                
    return ng

pg = None
while data != pg:
    pg = data
    data = cycle2(data)

print(nonesum(flatten(data)))
