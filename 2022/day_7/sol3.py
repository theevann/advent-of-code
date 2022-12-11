import sys
from collections import defaultdict

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    

current = ["/"]
sizes = defaultdict(int)
for l in data:
    l = l.split()
    if l == ["$", "cd", "/"]: current = ["/"]
    elif l == ["$", "cd", ".."]: current.pop()
    elif l[:2] == ["$", "cd"]: current.append(l[2])
    elif l == ["$", "ls"]: pass
    elif l[0] == "dir": pass
    else:
        for i in range(len(current)):
            name = "/".join(current[:i+1])
            sizes[name] += int(l[0])

# Part 1
print(sum(sz for sz in sizes.values() if sz <= 100000))

# Part 2
to_free = sizes["/"] - 40000000
print(min(filter(lambda sz: sz >= to_free, sizes.values())))