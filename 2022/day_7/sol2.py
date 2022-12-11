from functools import reduce
import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    

dirs = {}
current = []
for l in data:
    l = l.split()
    if l[0] == "$":
        if l[1] == "ls":
            continue
        if l[2] == "/":
            current = []
        elif l[2] == "..":
            current = current[:-1]
        else:
            current += [l[2]]
    else:
        cd = reduce(lambda x,y: x[y], current, dirs)
        cd[l[1]] = {} if l[0] == "dir" else int(l[0])

    
all_sizes = []
def visit(d):
    sz = sum(v if isinstance(v, int) else visit(v) for v in d.values())
    all_sizes.append(sz)
    return sz

visit(dirs)
all_sizes = sorted(all_sizes)

# Part 1
print(sum(sz for sz in all_sizes if sz <= 100000))

# Part 2
to_free = all_sizes[-1] - 40000000
for sz in all_sizes:
    if sz >= to_free:
        print(sz)
        break