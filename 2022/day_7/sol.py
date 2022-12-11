import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    

dirs = {"/":{}}
current = ["/"]
for l in data:
    l = l.split()
    if l[0] == "$":
        if l[1] == "ls":
            continue
        if l[2] == "/":
            current = ["/"]
        elif l[2] == "..":
            current = current[:-1]
        else:
            current += [l[2]]
    else:
        cd = dirs
        for c in current:
            cd = cd[c]
        cd[l[1]] = {} if l[0] == "dir" else int(l[0])


def compute_size(d):
    if isinstance(d, int):
        return d
    return sum(compute_size(v) for v in d.values())
    
all_dirs = {}
def visit(d, name):
    all_dirs[name] = compute_size(d)
    for k, v in d.items():
        if not isinstance(v, int):
            visit(v, name + k +"/")


visit(dirs["/"], "/")

# Part 1
print(sum(sz for sz in all_dirs.values() if sz <= 100000))

# Part 2
to_free = all_dirs["/"] - 40000000
for sz in sorted(all_dirs.values()):
    if sz >= to_free:
        print(sz)
        break