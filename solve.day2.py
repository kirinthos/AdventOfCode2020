#!/usr/local/bin/python3

with open('data.input', 'r') as f:
    data = [l.strip() for l in f.readlines()]

def in_range(v, l, h):
    return v >= l and v <= h

def process_password(l):
    policy, password = l.split(': ')
    r, c = policy.split(' ')
    low, high = map(int, r.split('-'))
    return in_range(password.count(c), low, high)

#print(sum(map(process_password, data)))

def process_password_2(l):
    policy, password = l.split(': ')
    r, c = policy.split(' ')
    low, high = map(int, r.split('-'))
    return (password[low-1] == c) != (password[high-1] == c)

print(sum(map(process_password_2, data)))
