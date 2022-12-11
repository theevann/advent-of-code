import numpy as np


data = np.loadtxt("input", dtype=int, delimiter=",")
data = np.array([16,1,2,0,4,2,7,1,2,14])

# Part 1
print(int(np.sum(np.abs(data - np.round(np.median(data))))))


# Part 2 (Smart)
print(np.mean(data) + 0.5)
x = np.abs(data - np.round(np.mean(data) + 0.5))
print(int(np.sum(x * (x+1) / 2)))

# Part 2 (Brute)
min_cost = None
min_i = None
for i in range(np.min(data), np.max(data)):
    x = np.abs(data - i)
    cost = np.sum(x * (x+1) / 2)
    # print(i, cost)
    if min_cost is None or cost < min_cost:
        min_cost = cost
        min_i = i
        
print(min_i, int(min_cost))
        
    
