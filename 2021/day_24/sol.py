import sys, re
import numpy as np
from collections import Counter, defaultdict
from functools import lru_cache

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

def floats(inp: str = None):
    return map(float, re.findall(r"-?\d+(?:\.\d*)?", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    
data = [[x for x in y.split()] for y in data]


def apply(idx, dt, inp, reg):
    if idx == len(dt):
        return reg
    
    op, *vs = dt[idx]
    register = {
        "w": reg[0],
        "x": reg[1],
        "y": reg[2],
        "z": reg[3],
    }
    
    if op == "inp":
        register[vs[0]] = int(inp[0])
        inp = inp[1:]
    else:
        v1 = vs[0]
        v2 = int(vs[1]) if vs[1] not in register else register[vs[1]]
        
        if op == "mul":
            register[v1] *= v2
        elif op == "add":
            register[v1] += v2
        elif op == "mod":
            register[v1] %= v2
        elif op == "div":
            register[v1] //= v2
        elif op == "eql":
            register[v1] = int(register[v1] == v2)
    
    reg = tuple(register[x] for x in "wxyz")
    return apply(idx+1, dt, inp, reg)


@lru_cache(20000)
def call_apply(idx, idx2, inp, reg):
    return apply(idx, ndata[idx2], inp, reg)

ndata = []
tdata = []
for d in data:
    if d[0] == "inp":
        ndata.append(tdata)
        tdata = []
    tdata.append(d)
ndata.append(tdata)
ndata = ndata[1:]
    
     
@lru_cache(None)
def reach(idx, goal_z):
    if idx < 0:
        return set([0])
       
    pool_in_z = [
        goal_z,
        *list(range(goal_z*26, goal_z*26+30)),
        *list(range(max(0,goal_z-26), goal_z)),
        *list(range(max(0,goal_z//26-2), goal_z//26+2)),
    ]
    
    v = set()
    for nb in range(1,10):
        for z in pool_in_z:
            *_, out_z = call_apply(0, idx, str(nb), (0,0,0,z))
            if out_z == goal_z:
                o = reach(idx-1, z)
                v.update(oo + nb*10**(13-idx) for oo in o)
    return v

r = reach(len(ndata)-1, 0)
print(max(r))
print(min(r))
# print(reach.cache_info())
print(call_apply.cache_info())