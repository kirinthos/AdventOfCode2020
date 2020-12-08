#!/usr/local/bin/python3

import math
import re
from functools import reduce
from itertools import groupby
from pprint import pprint

from common import flatten, partition, read_input

import numpy as np

data = read_input('data.input.day7')

# adjective color bags contain <number> adjective color bag...
bag_re = re.compile(r'(\d+) (\w+ \w+) bags?')
def parse(l):
    s, d = l.split(' bags contain ')
    return (s, list(partition([m for matches in bag_re.findall(d) for m in matches], 2)))
data = dict(parse(l) for l in data)

# i'm going to take a random guess and say this might be a graph problem
# but for part 1, we only need a tree

class Node(object):
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []

    def __repr__(self):
        return f'<Node: {self.name}>'

    def add_child(self, n, weight):
        self.children.append((n, weight))
        n.parents.append(self)


# TODO: i want a functional way to do this :( but i'm not super interested in wasting time on it
node_map = {k: Node(k) for k in data.keys()}
goldies = []
for k, nodes in data.items():
    for weight, name in nodes:
        if name == 'shiny gold':
            goldies.append(k)
        node_map[k].add_child(node_map[name], int(weight))


def walk_parents(n):
    if len(n.parents) == 0:
        return [n]
    return [n] + flatten(walk_parents(p) for p in n.parents)

#containers = flatten(walk_parents(node_map[g]) for g in goldies)
#print(len(set(containers)))

# part 2
# how many bags in a shiny gold bag?
def descend(node):
    if not node.children:
        return 0
    return sum((c[1] + c[1] * descend(c[0])) for c in node.children)

print(descend(node_map['shiny gold']))
