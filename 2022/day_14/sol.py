import sys, re
import numpy as np

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()
    
data = [[list(ints(x)) for x in y.split("->")] for y in data]
 
# 0 = AIR
# 1 = ROCK
# 2 = SAND

min_depth = 0
def read_map(data):
    global min_depth
    min_depth = 0
    maps = np.zeros((500, 1000))
    for l in data:
        for i in range(len(l)-1):
            start = l[i]
            end = l[i+1]
            if start[0] == end[0]:
                a = min(start[1], end[1])
                b = max(start[1], end[1])
                for j in range(a, b+1):
                    maps[j, start[0]] = 1
                min_depth = max(b, min_depth)
            else:
                a = min(start[0], end[0])
                b = max(start[0], end[0])
                for j in range(a, b+1):
                    maps[start[1], j] = 1
                min_depth = max(start[1], min_depth)
    return maps

# print(min_depth)
# print(maps[:13, 490:504])
# exit()
    
def find_place():
    moves = True
    current = (0, 500)
    while moves:
        if current[0] > min_depth+3:
            current = None
            moves = False
        elif maps[current[0]+1, current[1]] == 0:
            current = (current[0]+1, current[1])
        elif maps[current[0]+1, current[1]-1] == 0:
            current = (current[0]+1, current[1]-1)
        elif maps[current[0]+1, current[1]+1] == 0:
            current = (current[0]+1, current[1]+1)
        else:
            moves = False
    return current
    

# Part 1
maps = read_map(data)
for i in range(100000):
    current = find_place()
    if current is None:
        break
    maps[current] = 2
print(i)


# Part 2
maps = read_map(data)
for j in range(1000):
    maps[min_depth+2, j] = 1
    
for i in range(100000):
    current = find_place()
    if current == (0, 500):
        break
    maps[current] = 2
print(i+1)