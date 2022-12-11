import numpy as np

raw_data = np.loadtxt("input", dtype=int, delimiter="\n")
print("raw_data:", raw_data)

# PART 1
count = 0
for i in range(1, len(raw_data)):
    if raw_data[i] > raw_data[i - 1]:
        count += 1
print(count)

# PART 2
count = 0
cumsum = np.cumsum(raw_data)
for i in range(4, len(raw_data)):
    if cumsum[i] - cumsum[i - 3] > cumsum[i-1] - cumsum[i - 4]:
        count += 1
print(cumsum)
print(count)