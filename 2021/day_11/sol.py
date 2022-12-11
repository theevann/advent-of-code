import numpy as np


with open('input', 'r') as f:
    orig_data = f.read().splitlines()
orig_data = np.array([[int(x) for x in y] for y in orig_data])


# Part 1
all_flashes = 0
data = orig_data.copy()
for s in range(100):
    flash_map = np.zeros_like(data)
    data += 1
    
    flash = True
    while flash:
        flash = False
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i,j] > 9:
                    flash = True
                    flash_map[i,j] = 1
                    
                    data[max(i-1,0):i+2, max(j-1,0):j+2] += 1 - flash_map[max(i-1,0):i+2, max(j-1,0):j+2]
                    data[i,j] = 0
                    all_flashes += 1
print(all_flashes)


# Part 2
data = orig_data.copy()
for step in range(1000):
    flashes = np.zeros_like(data)
    data += 1
    
    flash = True
    while flash:
        flash = False
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i,j] > 9:
                    flash = True
                    flashes[i,j] = 1
                    
                    data[max(i-1,0):i+2, max(j-1,0):j+2] += + 1 - flashes[max(i-1,0):i+2, max(j-1,0):j+2]
                    data[i,j] = 0
    
    if data.sum() == 0:
        break
print(step + 1)