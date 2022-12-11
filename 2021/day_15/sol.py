import numpy as np
from collections import Counter
from queue import PriorityQueue

with open('input', 'r') as f:
    data = f.read().splitlines()
    data = np.array([[int(x) for x in y] for y in data])
    

# Part 1
def find_cheapest():
    R = len(data)
    C = len(data[0])

    r,c = R-1, C-1
    to_process = PriorityQueue()
    to_process.put((data[r,c], (r,c)))
    cheapest = {}
    cheapest[(r,c)] = data[r,c]

    while not to_process.empty():
        r,c = to_process.get()[1]
            
        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
            if 0 <= r+dr < R and 0 <= c+dc < C:
                new_cost = data[r+dr,c+dc] + cheapest[r,c]
                if (r+dr,c+dc) not in cheapest or new_cost < cheapest[r+dr,c+dc]:
                    to_process.put((new_cost, (r+dr,c+dc)))
                    cheapest[(r+dr,c+dc)] = new_cost

    print(cheapest[0,0]-data[0,0])

find_cheapest()


# Part 2
data = np.concatenate([((data+i)-1)%9+1 for i in range(5)], axis=0)
data = np.concatenate([((data+i)-1)%9+1 for i in range(5)], axis=1)
find_cheapest()