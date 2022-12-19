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
    
dataset = set(tuple(ints(y)) for y in data)


# Part 1
def get_neighbours(x, y, z):
    yield from ((x, y, z-1), (x, y, z+1), (x, y-1, z), (x, y+1, z), (x-1, y, z), (x+1, y, z))

faces = sum(d not in dataset for c in dataset for d in get_neighbours(*c))
print(faces)


# Part 2
mx = max(x for l in dataset for x in l) + 1
mn = min(x for l in dataset for x in l) - 1
sys.setrecursionlimit(10000)

explored = set()
def explore(c):
    explored.add(c)
    for d in get_neighbours(*c):
        if mx >= max(d) and min(d) >= mn and d not in dataset and d not in explored:
            explore(d)
explore((0,0,0))

faces = sum(d in explored for c in dataset for d in get_neighbours(*c))
print(faces)