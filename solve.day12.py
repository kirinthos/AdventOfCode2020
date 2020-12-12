#!/usr/local/bin/python3

import math
import re
from functools import partial, reduce
from itertools import combinations
from pprint import pprint

from common import add, read_input, rotate_around_pt, sub

import numpy as np

data = [(l[0], int(l[1:])) for l in read_input('data.input.day12')]

dirmap = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}
ship = ((0, 0), 0) # 0degress = right = east

def step(ship, n):
    key, value = n
    if key == 'L':
        ship = (ship[0], ship[1] + value)
    elif key == 'R':
        ship = (ship[0], ship[1] - value)
    elif key == 'F':
        r = np.deg2rad(ship[1])
        ship = (add(ship[0], (np.cos(r) * value, math.sin(r) * value)), ship[1])
    else:
        d = dirmap[key]
        ship = (add(ship[0], (d[0] * value, d[1] * value)), ship[1])
    return ship

#print(sum(map(abs, reduce(step, data, ship)[0])))

# part 2
ship = (0, 0)
way = (10, 1)

def step2(pts, n):
    ship, way = pts
    key, value = n
    if key == 'L':
        way = rotate_around_pt(ship, way, value)
    elif key == 'R':
        way = rotate_around_pt(ship, way, -value)
    elif key == 'F':
        v = list(sub(way, ship))
        vs = [v] * value
        ship = list(reduce(lambda acc, n: add(acc, n), vs, ship))
        way = add(ship, v)
    else:
        d = dirmap[key]
        way = list(add(way, (d[0] * value, d[1] * value)))
    return ship, way

print(sum(map(abs, reduce(step2, data, (ship, way))[0])))
