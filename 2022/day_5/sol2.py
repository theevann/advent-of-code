import sys, re
from copy import deepcopy


def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()

# Parse input
for i,l in enumerate(data):
    if "[" not in l:
        end = i
        break
    data[i] = "".join(l[1::4])
col = [[c for c in l[::-1] if c != " "] for l in zip(*data[:end])]

# Parse and apply moves - Part 1
col_p1 = deepcopy(col)
for l in data[end+2:]:
    q,s,d = ints(l)
    col_p1[d-1] += col_p1[s-1][-q:][::-1]
    col_p1[s-1] = col_p1[s-1][:-q]
print("".join([i[-1] for i in col_p1]))

# Parse and apply moves - Part 2
col_p2 = deepcopy(col)
for l in data[end+2:]:
    q,s,d = ints(l)
    col_p2[d-1] += col_p2[s-1][-q:]
    col_p2[s-1] = col_p2[s-1][:-q]
print("".join([i[-1] for i in col_p2]))