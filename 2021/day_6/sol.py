import numpy as np


# with open('input', 'r') as f:
#     w, h = [int(x) for x in next(f).split()]
#     data = [[int(x) for x in line.split()] for line in f]
# print(data)

    
# raw_data = np.array([3,4,3,1,2], dtype=int)
raw_data = np.loadtxt("input", dtype=int, delimiter=",")


# PART 1
data = raw_data.copy()
for day in range(80):
    mask = data == 0
    data[~mask] -= 1
    data[mask] = 6
    data = np.concatenate([data, [8]*sum(mask)])
print(len(data))


# PART 2
data = raw_data.copy()

my_list = np.array([0]*9)
for i, count in zip(np.unique(data, return_counts=True)):
    my_list[i] = count

for day in range(256):
    new_list = np.array([0]*9)
    for i in range(1, len(my_list)):
        new_list[i-1] = my_list[i]
    new_list[6] += my_list[0]
    new_list[8] += my_list[0]
    my_list = new_list
print(np.sum(my_list))