import numpy as np

map_idc = []
splits = []
with open('input', 'r') as f:
    data = f.read().splitlines()
    mode = 0
    for l in data:
        if l != "":
            if mode == 0:
                map_idc.append([int(x) for x in l.split(",")])
            else:
                a, b = l.split("=")
                splits.append((a[-1], int(b)))
        else:
            mode = 1

# Part 1
def fold(idc, dir, s):
    new_idc = set()
    for (x,y) in idc:
        if dir == "x":
            if x <= s:
                new_idc.add((x, y))
            elif x >= s:
                new_idc.add((2*s - x,y))
        elif dir == 'y':
            if y <= s:
                new_idc.add((x, y))
            elif y >= s:
                new_idc.add((x, 2*s - y))
    return new_idc

print(len(fold(map_idc, *splits[0])))


# Part 2
for dir, s in splits:
    map_idc = fold(map_idc, dir, s)

mx, my = np.max(list(map_idc), axis=0) + 1
map = np.zeros((my, mx), np.uint8)
for x, y in map_idc:
    map[y, x] = 255
    
for l in map:
    for p in l:
        print("#" if p else " ", end="")
    print()

# from PIL import Image
# Image.fromarray(map).save('letters.png')