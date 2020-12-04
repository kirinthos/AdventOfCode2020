#!/usr/local/bin/python3

from common import prod

from math import ceil

with open('data.input.day3', 'r') as f:
    data = [[*l.strip()] for l in f.readlines()]

class RepeatMap(object):
    def __init__(self, grid):
        self.grid = grid
        self.domain = len(self.grid[0])
        self.range = len(self.grid)

    def lookup(self, x, y):
        if isinstance(x, tuple):
            x, y = x

        return self.grid[y % self.range][x % self.domain]

m = RepeatMap(data)
path = [m.lookup(3 * i, i) for i in range(m.range)]
len_path = len(list(filter(lambda v: v == '#', path)))
#print(len_path)

# Day two
def trees_on_path(m, slope):
    path = [m.lookup(slope[0] * i, slope[1] * i) for i in range(0, ceil(m.range / slope[1]))]
    return len(list(filter(lambda v: v == '#', path)))

print(prod(trees_on_path(m, slope) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
