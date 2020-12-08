#!/usr/local/bin/python3

import math
import re
from functools import reduce
from itertools import groupby
from pprint import pprint

from common import flatten, partition, read_input

import numpy as np

def process(l):
    op, v = l.split(' ')
    v = int(v)
    return op, v
data = [process(l) for l in read_input('data.input.day8')]

tape = data # you know, like a program

class InfiniteException(Exception):
    pass

def run(tape):
    acc = 0 # 5 # for problem
    ip = 0

    # part 1 requires us to halt when an instruction is visited a second time
    l = len(tape)
    visits = [0] * l
    while True:
        if ip == l:
            break # part 2 success
        if visits[ip]:
            raise InfiniteException() # part 2
            break

        visits[ip] += 1

        op, v = tape[ip]
        if op == 'acc':
            acc += v
        elif op == 'jmp':
            ip += v
            continue # don't increment IP
        elif op == 'nop':
            pass
        else:
            raise Exception('unknown instruction')
        ip += 1

    print('success')
    return acc

#print(run(tape))

# part 2
# we have to run the tape over and over, changing one instruction at a time

for i, (op, v) in enumerate(tape):
    try:
        if op == 'nop':
            tape2 = tape[:]
            tape2[i] = ('jmp', v)
            #print(tape[i], tape2[i])
            print(run(tape2))
        elif op == 'jmp':
            tape2 = tape[:]
            tape2[i] = ('nop', v)
            print(run(tape2))
    except InfiniteException: 
        pass
    except IndexError:
        pass
