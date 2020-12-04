#!/usr/local/bin/python3

from functools import reduce
from pprint import pprint

from common import read_input

data = read_input('data.input.day4')

# fold up into one-line records
def foldem(acc, n):
    if n == '': # split records
        acc.append('')
    else:
        acc[-1] = (acc[-1] + f' {n}').strip()
    return acc

data = reduce(foldem, data, [''])

# should this become a class for later problems?
def tokenize(l):
    # split each space-delimited segment into pairs
    return [s.split(':') for s in l.split(' ')]

data = list(map(tokenize, data))

required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) #omit 'cid'

def check(p):
    keys = set(map(lambda v: v[0], p))
    return len(required - keys) == 0

#print(sum(map(check, data)))

# second part, building validation rules
import re

year_re = re.compile(r'(\d\d\d\d)')
height_re = re.compile(r'(\d+)(cm|in)')
hair_re = re.compile(r'(#[0-9a-f]{6})')
eye_re = re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)')
pid_re = re.compile(r'(\d{9})')
cid_re = re.compile('(.*)')

def byr(v):
    y = int(v)
    return y >= 1920 and y <= 2002

def iyr(v):
    y = int(v)
    return y >= 2010 and y <= 2020

def eyr(v):
    y = int(v)
    return y >= 2020 and y <= 2030

def hgt(h, s):
    h = int(h)
    return (s == 'cm' and h >= 150 and h <= 193) or (s == 'in' and h >= 59 and h <= 76)

def hcl(v):
    return True

def ecl(v):
    return True

def pid(v):
    return True

def cid(v):
    return True

prop_map = {
    'byr': year_re,
    'iyr': year_re,
    'eyr': year_re,
    'hgt': height_re,
    'hcl': hair_re,
    'ecl': eye_re,
    'pid': pid_re,
    'cid': cid_re,
}

def check_valid(item):
    k, v = item
    g = prop_map[k].fullmatch(v)
    return g is not None and globals()[k](*g.groups())

def check_passport(p):
    return check(p) and all(map(check_valid, p))

print(sum(map(check_passport, data)))
