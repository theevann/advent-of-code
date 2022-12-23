import sys, re
import numpy as np
from collections import Counter, defaultdict
from functools import lru_cache, reduce
from itertools import combinations
from copy import deepcopy

AMAX = float("inf")

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()
    
data = [[x for x in y.split()] for y in data]
data = {y[1]: [int(y[4][5:-1]), [x.strip(",") for x in y[9:]]] for y in data}



to_release = set(l for l, (p, ls) in data.items() if p > 0)


def min_time_to_node(start, goal, visited):
    neighbours = data[start][1]
    visited.add(start)
    if goal in neighbours:
        return 1
    
    time = AMAX
    for n in neighbours:
        if n not in visited:
            t = 1 + min_time_to_node(n, goal, visited.copy())
            time = min(t, time)
    return time


times = {
    v1: {
        v2: min_time_to_node(v1, v2, set()) for v2 in to_release if v1 != v2
    } for v1 in ["AA", *to_release]
}


@lru_cache(maxsize=None)
def max_release(current, left_to_release, time_left):
    time_left -= (current != "AA")

    max_releasable = 0
    for next_valve in left_to_release:
        if times[current][next_valve] <= time_left:
            releasable = max_release(next_valve, frozenset(left_to_release - {next_valve}), time_left - times[current][next_valve])
            
            max_releasable = max(max_releasable, releasable)
          
    return max_releasable + data[current][0] * time_left


# Part 1
print(max_release("AA", frozenset(to_release), 30))

# Part 2
max_releasable = 0
for i in range(1, len(to_release) // 2 + 1):
    # print(i, "/", len(to_release) // 2)
    for c in combinations(to_release, i):
        v1 = max_release("AA", frozenset(to_release - set(c)), 26)
        v2 = max_release("AA", frozenset(c), 26)
        max_releasable = max(max_releasable, v1+v2)
print(max_releasable)