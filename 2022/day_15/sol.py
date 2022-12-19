import sys, re
import numpy as np
from collections import Counter, defaultdict
from functools import lru_cache, reduce
from copy import deepcopy

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)
prod = lambda array: reduce(lambda a, b: a * b, array, 1)

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

def floats(inp: str = None):
    return map(float, re.findall(r"-?\d+(?:\.\d*)?", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()
    
data = [list(ints(y)) for y in data]

goal = 10
goal = 2000000

occupied = []
mx, mn = 0, 0
for l in data:
    xs, ys, xb, yb = l
    d = abs(xs - xb) + abs(ys - yb)
    left = d - abs(ys - goal)
    if left >= 0:
        occupied.append((xs-left, xs+left))
        mx = max(xs+left, mx)
        mn = min(xs-left, mn)

X = np.zeros(9000000)
for a,b in occupied:
    X[a+2000000:b+2000000] = 1
print(int(X.sum()))


# Part 2

def merge_ranges(occupied):
    occupied.sort()
    current = 0
    while current < len(occupied)-1:
        if occupied[current+1][0] <= occupied[current][1]:
            occupied[current] = (occupied[current][0] , max(occupied[current][1], occupied[current+1][1]))
            del occupied[current+1]
        else:
            current += 1
    return occupied
    

mx = 20
mx = 4000000

for i in range(mx, -1, -1):
    occupied = []
    for l in data:
        xs, ys, xb, yb = l
        d = abs(xs - xb) + abs(ys - yb)
        left = d - abs(ys - i)
        if left >= 0:
            occupied.append((xs-left, xs+left))
    occupied = merge_ranges(occupied)
    if len(occupied) == 2:
        print((occupied[0][1]+1)*4000000 + i)
        break