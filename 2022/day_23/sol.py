import os, sys
from collections import Counter
from functools import lru_cache


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()

elves = [(c, r) for r, line in enumerate(data) for c, point in enumerate(line) if point == "#"]


@lru_cache(maxsize=None)
def get_all_neighbours(c, r):
    return [(c + i, r + j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

def get_north_neighbours(c, r):
    return [(c + i, r - 1) for i in range(-1, 2)]

def get_south_neighbours(c, r):
    return [(c + i, r + 1) for i in range(-1, 2)]

def get_east_neighbours(c, r):
    return [(c + 1, r + i) for i in range(-1, 2)]

def get_west_neighbours(c, r):
    return [(c - 1, r + i) for i in range(-1, 2)]

dirs = [get_north_neighbours, get_south_neighbours, get_west_neighbours, get_east_neighbours]


def make_proposition(e, order, elves_set):
    if all(not (ne in elves_set) for ne in get_all_neighbours(*e)):
        return None
    
    for i in range(4):
        d = dirs[(i+order) % 4](*e)
        if all(not (ne in elves_set) for ne in d):
            return d[1]
        
    return None
    

def print_map(elves):
    min_c = min(elves, key=lambda x: x[0])[0]
    max_c = max(elves, key=lambda x: x[0])[0]
    min_r = min(elves, key=lambda x: x[1])[1]
    max_r = max(elves, key=lambda x: x[1])[1]
    
    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if (c, r) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print()

    
for round in range(1000):
    elves_set = set(elves)
    props = [make_proposition(elve, round, elves_set) for elve in elves]
    
    count = Counter(props)
    if len(count) == 1:
        break
    
    elves = [e if (count[p] > 1 or p is None) else p for p, e in zip(props, elves)]
    
    if round+1 == 10:
        r1 = min(elves, key=lambda x: x[1])[1]
        r2 = max(elves, key=lambda x: x[1])[1]
        c1 = min(elves, key=lambda x: x[0])[0]
        c2 = max(elves, key=lambda x: x[0])[0]
        print((r2-r1+1) * (c2-c1+1) - len(elves))
    
    # os.system('clear')
    # print_map(elves)
    # input()

print(round+1)