import sys
import numpy as np

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()

algo = [x == "#" for x in data[0]]
img = np.array([[x == "#" for x in y] for y in data[2:]])


kernel = np.array([1 << (8-i) for i in range(9)]).reshape(3,3)
def enhance(img, pad):
    img = np.pad(img, 2, 'constant', constant_values=pad)
    new_img = np.ones_like(img) * (1-pad)
    for i in range(1, len(img)-1):
        for j in range(1, len(img[0])-1):
            value = (kernel * img[i-1:i+2, j-1:j+2]).sum()
            new_img[i,j] = algo[value]
    return new_img
 
# Part 1 & 2
for step in range(50):
    img = enhance(img, pad=step%2)
    if step == 1: print(img.sum())

print(img.sum())