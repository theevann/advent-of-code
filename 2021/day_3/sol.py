import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
max_b = len(max(data, key=len))
data = ["0"*(max_b-len(x))+x for x in data]


# Part 1
g = 0
e = 0
for i in range(max_b):
    c = sum(int(n[max_b - 1 - i]) for n in data)

    if c > len(data)/2:
        g += 1<<i
    else:
        e += 1<<i

print(e*g)

# Part 2
data_1 = data_2 =data

for i in range(max_b):
    keep_condition = sum(int(n[i]) for n in data_1) >= len(data_1)/2
    data_1 = [d for d in data_1 if int(d[i]) == keep_condition]

    if len(data_1) == 1:
        break

for i in range(max_b):
    keep_condition = sum(int(n[i]) for n in data_2) < len(data_2)/2
    data_2 = [d for d in data_2 if int(d[i]) == keep_condition]
    
    if len(data_2) == 1:
        break
    
o2 = int(data_1[0], 2)
co2 = int(data_2[0], 2)
print(o2*co2)