import sys, re
import numpy as np
from collections import Counter, defaultdict
from functools import lru_cache, reduce
from copy import deepcopy

sys.setrecursionlimit(5000)

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
    
data = [[x for x in y] for y in data]
# data = np.loadtxt("input", dtype=int, delimiter="\n")

cost_so_far = [[AMAX]*len(data[0]) for _ in range(len(data))]


def cost(A, B):
    if A == "S":
        A = "a"
    elif A == "E":
        A = "z"
    if B == "S":
        B = "a"
    if B == "E":
        B = "z"
    return ord(A) - ord(B)


def get_cost_so_far_1(x, y, current_cost=0):
    if cost_so_far[x][y] > current_cost:
        cost_so_far[x][y] = current_cost
        for (i,j) in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if not (i < 0 or i >= len(data) or j < 0 or j >= len(data[0])) and (cost(data[i][j], data[x][y]) <= 1):
                get_cost_so_far_1(i, j, current_cost=current_cost+1)

def get_cost_so_far_2(x, y, current_cost=0):
    if cost_so_far[x][y] > current_cost:
        cost_so_far[x][y] = current_cost
        for (i,j) in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if not (i < 0 or i >= len(data) or j < 0 or j >= len(data[0])) and (cost(data[i][j], data[x][y]) >= -1):
                get_cost_so_far_2(i, j, current_cost=current_cost+1)


cost_so_far = [[AMAX]*len(data[0]) for _ in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            get_cost_so_far_1(i, j, current_cost=0)
            for k in range(len(data)):
                for l in range(len(data[0])):
                    if data[k][l] == 'E':
                        print(cost_so_far[k][l])


cost_so_far = [[AMAX]*len(data[0]) for _ in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'E':
            get_cost_so_far_2(i, j, current_cost=0)
        
new_min = AMAX
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'a':
            new_min = min(cost_so_far[i][j], new_min)
print(new_min)