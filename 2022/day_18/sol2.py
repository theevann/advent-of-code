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
    
data = [tuple(ints(y)) for y in data]
dataset = set(data)
# dataset = set(tuple(ints(y)) for y in data)

# Part 1
faces = set()
for c in data:
    cx, cy, cz = c
    s = set(((cx, cy, cz-0.5), (cx, cy, cz+0.5),
             (cx, cy-0.5, cz), (cx, cy+0.5, cz),
             (cx-0.5, cy, cz), (cx+0.5, cy, cz)))
    faces ^= s
print(len(faces))


# Part 2
mx = max(x for l in dataset for x in l) + 1
mn = min(x for l in dataset for x in l) - 1
sys.setrecursionlimit(10000)

explored = set()
def explore(x, y, z):
    explored.add((x, y, z))
    for i, j, k in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
        nx, ny, nz = x+i, y+j, z+k
        if mx >= nx >= mn and mx >= ny >= mn and mx >= nz >= mn:
            if (nx, ny, nz) not in dataset and (nx, ny, nz) not in explored:
                explore(nx, ny, nz)

explore(0,0,0)

faces = 0
for c in dataset:
    cx, cy, cz = c
    s = set(((cx, cy, cz-1), (cx, cy, cz+1), (cx, cy-1, cz), (cx, cy+1, cz), (cx-1, cy, cz), (cx+1, cy, cz)))
    faces += sum(c in explored for c in s)
print(faces)