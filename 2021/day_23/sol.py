import sys

AMIN = -float("inf")
AMAX = float("inf")

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    
amap = [[x for x in y] for y in data]
lmap = [[False,]*len(amap[0]) for i in range(len(amap))]

# Get all positions of all letters not locked one by one
def can_move(amap, lmap):
    for i, l in enumerate(amap):
        for j, x in enumerate(l):
            if x in ["A", "B", "C", "D"]:
                if not lmap[i][j]:
                    yield i,j,x

# Get all positions reachable from i,j with distance
def possible_moves(i,j, amap, visited=[]):
    positions = []
    for k,l in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
        if amap[k][l] == "." and (k,l) not in visited:
            positions += [(k,l,0)]
            positions += possible_moves(k, l, amap, visited + [(i,j)])
    positions = [(i,j,c+1) for i,j,c in positions]
    return positions

def is_end(amap):
    for i in range(2, len(amap)-1):
        for x, j in dests.items():
            if amap[i][j] != x:
                return False
    return True

def printm(amap):
    for l in amap:
        for c in l:
            print(c, end='')
        print("")

def get_in_cache(amap, lmap):
    key = tuple(x for d in [amap, lmap] for y in d for x in y)
    return cache.get(key, None)

def put_in_cache(amap, lmap, value):
    key = tuple(x for d in [amap, lmap] for y in d for x in y)
    cache[key] = value


dests = {"A": 3, "B": 5, "C": 7, "D": 9 }
costs = {"A": 1, "B": 10, "C": 100, "D": 1000 }
cache = {}

def solve(amap, lmap):
    cache = get_in_cache(amap, lmap)
    if cache is not None:
        return cache
    
    if is_end(amap):
        return 0
    
    min_cost = AMAX
    for i,j,x in can_move(amap, lmap):
        for k,l,c in possible_moves(i,j, amap):
            if k == 1 and (i == 1 or l in [3,5,7,9]):
                continue
            elif k > 1:
                if l != dests[x]:
                    continue
                if any(amap[m][l] != x for m in range(k+1, len(amap)-1)):
                    continue

            amap[i][j], amap[k][l] = amap[k][l], amap[i][j]
            a,b = lmap[i][j], lmap[k][l]
            lmap[i][j], lmap[k][l] = False, k > 1
            
            cost = solve(amap, lmap)
            min_cost = min(cost + c*costs[x], min_cost)
            
            amap[i][j], amap[k][l] = amap[k][l], amap[i][j]
            lmap[i][j], lmap[k][l] = a,b
            
    put_in_cache(amap, lmap, min_cost)
    return min_cost

print(solve(amap, lmap))