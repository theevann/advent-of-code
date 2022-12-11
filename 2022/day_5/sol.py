import sys, re

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

def floats(inp: str = None):
    return map(float, re.findall(r"-?\d+(?:\.\d*)?", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    

col = [[] for i in range(9)]
moves_p = []

for i,l in enumerate(data):
    if "[" not in l:
        start = i+2
        break
    
    m = l.replace(" [", "").replace("] ", " ").replace("   ", "#").replace(" ", "").replace("[", "").replace("]", "")
    for j,_ in enumerate(m):
        if _ != "#":
            col[j].append(_)


for l in data[start:]:
    moves_p.append(list(ints(l)))

col_p1 = [i[::-1] for i in col]
for q,s,d in moves_p:
    col_p1[d-1] += col_p1[s-1][-q:][::-1]
    col_p1[s-1] = col_p1[s-1][:-q]
print("".join([i[-1] for i in col_p1 if i]))

col_p2 = [i[::-1] for i in col]
for q,s,d in moves_p:
    col_p2[d-1] += col_p2[s-1][-q:]
    col_p2[s-1] = col_p2[s-1][:-q]
print("".join([i[-1] for i in col_p2 if i]))