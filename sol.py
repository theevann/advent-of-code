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
    
# data = [[int(x) for x in y.split()] for y in data]
# data = np.loadtxt("input", dtype=int, delimiter="\n")

# print(data)
for l in data:
    print(l)