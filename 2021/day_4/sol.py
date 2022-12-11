import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
    
numbers = list(map(int, data[0].split(",")))
data = data[2:]

array = []
while len(data) > 0:
    array += [[[int(x) for x in y.strip().split()] for y in data[:5]]]
    data = data[6:]
array = np.array(array)


# Part 1
mask = np.zeros_like(array, dtype=bool)
idx = None
for n in numbers:
    mask |= (array == n)
    
    col = (mask.sum(axis=1) == 5)
    row = (mask.sum(axis=2) == 5)
    
    if row.sum() > 0:
        [idx], _ = row.nonzero()
    elif col.sum() > 0:
        [idx], _ = col.nonzero()
        
    if idx is not None:
        s = array[idx][~mask[idx]].sum()
        print(n * s)
        break
        


# Part 2
mask = np.zeros_like(array, dtype=bool)
for n in numbers:
    mask |= (array == n)
    
    col = (mask.sum(axis=1) == 5)
    row = (mask.sum(axis=2) == 5)
    
    idcs = list(row.nonzero()[0])
    idcs += list(col.nonzero()[0])
    idcs = sorted(list(set(idcs)), reverse=True)
        
    for idx in idcs:
        if len(array) > 1:
            array = np.delete(array, idx, axis=0)
            mask = np.delete(mask, idx, axis=0)
        else:
            s = array[idx][~mask[idx]].sum()
            print(n * s)
            exit()