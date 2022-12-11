import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
    data = [[[int(c) for c in a.split(",")] for a in x.split(" -> ")] for x in data]
 
 
# Part 1
map = np.zeros((1000, 1000))
for l in data:
    (y11, x11), (y12, x12) = l
    
    if x11 > x12:
        x11, y11, x12, y12 = x12, y12, x11, y11
    
    if x11 == x12:
        map[x11,min(y11, y12):max(y11,y12)+1] += 1
    elif y11 == y12:
        map[x11:x12+1, y11] += 1

print(np.sum(map > 1))

 
# Part 2
map = np.zeros((1000, 1000))
for l in data:
    (y11, x11), (y12, x12) = l
    
    if x11 > x12:
        x11, y11, x12, y12 = x12, y12, x11, y11
    
    range_y = range(min(y11, y12), max(y11,y12)+1)
    if y11 > y12:
        range_y = reversed(range_y)
    map[list(range(x11, x12+1)), list(range_y)] +=1

print(np.sum(map > 1))