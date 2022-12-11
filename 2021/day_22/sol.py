import sys, re
import numpy as np
from collections import Counter, defaultdict
from functools import lru_cache

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

def floats(inp: str = None):
    return map(float, re.findall(r"-?\d+(?:\.\d*)?", inp or sys.stdin.read()))

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()

todo = [y[:2] == "on" for y in data]
data = [list(ints(y)) for y in data]
# print(todo)
# print(data)

mask = np.zeros((100,100,100))
for i, (t, l) in enumerate(zip(todo, data)):
    # print(t, l)
    l = np.array(l)+50
    mask[l[0]:l[1]+1,l[2]:l[3]+1,l[4]:l[5]+1] = t
    print(i, int(mask.sum()))
    if i == 2:
        break
    
data = [[c[0]-0.5, c[1]+0.5, c[2]-0.5, c[3]+0.5, c[4]-0.5, c[5]+0.5] for c in data]


# from more_itertools import pairwise
# def create_cubes(a, b):
#     ax0,ax1,ay0,ay1,az0,az1 = a
#     bx0,bx1,by0,by1,bz0,bz1 = b
#     xs = sorted([ax0, ax1, bx0, bx1])
#     xs = [(xs[0], xs[1]-1), (xs[1], xs[2]), (xs[2]+1, xs[3])]
#     ys = sorted([ay0, ay1, by0, by1])
#     ys = [(ys[0], ys[1]-1), (ys[1], ys[2]), (ys[2]+1, ys[3])]
#     zs = sorted([az0, az1, bz0, bz1])
#     zs = [(zs[0], zs[1]-1), (zs[1], zs[2]), (zs[2]+1, zs[3])]
    
#     for x in (xs):
#         for y in (ys):
#             for z in (zs):
#                 if x[0] > x[1] or y[0] > y[1] or z[0] > z[1]:
#                     continue
#                 # print(x,y,z)
#                 yield (x[0], x[1], y[0], y[1], z[0], z[1])

# print(list(create_cubes(data[0], data[1])))
# print(list(create_cubes([1,4,1,3,1,1], [3,5,2,4,1,1])))

# def sliced(array):
#     for i in range(len(array)):
#         yield array[i],array[i]
#         if i+1 < len(array):
#             if array[i]+1 <= array[i+1]-1:
#                 yield array[i]+1,array[i+1]-1

def sliced(array):
    for i in range(len(array)-1):
        yield array[i],array[i+1]

# print(list(sliced([1,3, 4, 5])))

from more_itertools import split_before, split_after

# xs = sorted(list(set([x for c in data for x in c[:2]])))
# ys = sorted(list(set([x for c in data for x in c[2:4]])))
# zs = sorted(list(set([x for c in data for x in c[4:]])))

def create_cubes(array, limit=None):
    xs = sorted(list(set([x for c in array for x in c[:2]])))
    ys = sorted(list(set([x for c in array for x in c[2:4]])))
    zs = sorted(list(set([x for c in array for x in c[4:]])))
    *_, xss = split_before(xs, lambda x: x == limit[0], maxsplit=1)
    xss, *_ = split_after(xss, lambda x: x == limit[1], maxsplit=1)
    *_, yss = split_before(ys, lambda x: x == limit[2], maxsplit=1)
    yss, *_ = split_after(yss, lambda x: x == limit[3], maxsplit=1)
    *_, zss = split_before(zs, lambda x: x == limit[4], maxsplit=1)
    zss, *_ = split_after(zss, lambda x: x == limit[5], maxsplit=1)
    print(np.array(array))
    print()
    print(xss)
    print(yss)
    print(zss)
    # print("")
    
    for x in sliced(xss):
        for y in sliced(yss):
            for z in sliced(zss):
                # print(x,y,z)
                yield (x[0], x[1], y[0], y[1], z[0], z[1])
                

def intersect_any(array, a):
    for b in array:
        if intersect_cuboids(a,b):
            return True
    return False

def intersect_cuboids(a, b):
    ax0,ax1,ay0,ay1,az0,az1 = a
    bx0,bx1,by0,by1,bz0,bz1 = b
    
    return ax1 >= bx0 and bx1 >= ax0 and ay1 >= by0 and by1 >= ay0 and az1 >= bz0 and bz1 >= az0

def intersect(array, c, t):
    new_set = set()
    to_process = []
    # Select all in array that intersect with c
    for d in array:
        if intersect_cuboids(d, c):
            to_process.append(d)
        else:
            new_set.add(d)

    cubes = list(create_cubes([*to_process, c]))
    for d in cubes:
        if (t == 1):
            if intersect_cuboids(c, d) or intersect_any(to_process, d):
                new_set.add(d)
        else:
            if (not intersect_cuboids(c, d)) and intersect_any(to_process, d):
                new_set.add(d)
    print(c, len(new_set))
            
    return new_set


print()
all_cuboids = set()
for i, (t, d) in enumerate(zip(todo, data)):
    cubes = list(create_cubes([x for x in data if intersect_cuboids(x,d)], limit=d))
    for c in cubes:
        if t:
            all_cuboids.add(c)
        else:
            if c in all_cuboids:
                all_cuboids.remove(c)
    # print(i, len(all_cuboids))

    s = 0
    for c in all_cuboids:
        x0,x1,y0,y1,z0,z1 = c
        s += (x1-x0)*(y1-y0)*(z1-z0)
    print(i, int(s))
    # print(all_cuboids)
    print()
    
    
    if i == 2:
        break

# s = 0
# for c in create_cubes(data):
#     x0,x1,y0,y1,z0,z1 = c

#     status = 0
#     for t, d in zip(todo, data):
#         if intersect_cuboids(c, d):
#             status = t

#     if status == 1:
#         s += (x1-x0+1)*(y1-y0+1)*(z1-z0+1)
# print(s)



# s = 0
# cuboids = set()
# from tqdm import tqdm
# for t, d in tqdm(zip(todo, data)):
#     for c in create_cubes(d):
#         # print(c)
#         if t == 0 and c in cuboids:
#             cuboids.remove(c)
#         else:
#             cuboids.add(c)
  
# cuboids = set()     
# for i, (t, d) in enumerate(zip(todo, data)):
#     cuboids = intersect(cuboids, d, t)
#     if i == 1: break
        
# s = 0
# for c in cuboids:
#     x0,x1,y0,y1,z0,z1 = c
#     s += (x1-x0+1)*(y1-y0+1)*(z1-z0+1)
# print(s)