import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
    data = np.array([[int(x) for x in y] for y in data])

def is_lowpoint(i,j):
    lowpoint = True
    if i > 0:
        lowpoint &= data[i-1][j] > data[i][j] 
    if i < len(data)-1:
        lowpoint &= data[i+1][j] > data[i][j]
    if j > 0:
        lowpoint &= data[i][j-1] > data[i][j]
    if j < len(data[i])-1:
        lowpoint &= data[i][j+1] > data[i][j]
    return lowpoint


# Part 1
r = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if is_lowpoint(i,j):
            r += data[i][j] + 1

print(r)


# Part 2
def spread(i,j):
    s = 1
    data[i][j] = 10
    if i > 0 and data[i-1][j] < 9:
        s += spread(i-1,j)
    if j > 0 and data[i][j-1] < 9:
        s += spread(i,j-1)
    if i < len(data)-1 and data[i+1][j] < 9:
        s += spread(i+1,j)
    if j < len(data[i])-1 and data[i][j+1] < 9:
        s += spread(i,j+1)
    return s

sizes = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if is_lowpoint(i,j):
            sizes += [spread(i,j)]

sizes = sorted(sizes)
print(sizes[-3]*sizes[-2]*sizes[-1])
    
    
