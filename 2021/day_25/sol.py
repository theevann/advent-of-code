import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    
data = [[(x) for x in y] for y in data]

print(data)

def printm(emap,smap):
    for i in range(R):
        for j in range(C):
            if (i,j) in emap:
                print(">", end="")
            elif (i,j) in smap:
                print("v", end="")
            else:
                print(".", end="")
        print()
    print()

R, C = len(data), len(data[0])

emap = set()
smap = set()
for i, l in enumerate(data):
    for j, x in enumerate(l):
        if x == ">":
            emap.add((i,j))
        elif x == "v":
            smap.add((i,j))

# printm(emap,smap)

run = True
step = 0
while run:
    new_emap = set()
    new_smap = set()
    
    for i,j in emap:
        if (i, (j+1)%C) not in smap and (i, (j+1)%C) not in emap:
            new_emap.add((i, (j+1)%C))
        else:
            new_emap.add((i, j))
    
    for i,j in smap:
        if ((i+1)%R, j) not in smap and ((i+1)%R, j) not in new_emap:
            new_smap.add(((i+1)%R, j))
        else:
            new_smap.add((i, j))
            
    run &= (emap != new_emap) | (smap != new_smap)
    emap = new_emap
    smap = new_smap
    step += 1

print(step)

