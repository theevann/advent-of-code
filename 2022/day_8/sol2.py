import sys
import numpy as np

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()
    
nb = [[x for x in l] for l in data]
nb = np.array(nb)

s = 0
for c in range(len(nb)):
    for r in range(len(nb[c])):
        v = False
        v |= all(nb[c, r] > nb[:c, r])
        v |= all(nb[c, r] > nb[c+1:, r])
        v |= all(nb[c, r] > nb[c, :r])
        v |= all(nb[c, r] > nb[c, r+1:])
        s += int(v)
print(s)

m = 0
for c in range(1, len(nb)):
    for r in range(1, len(nb[c])):
        d = 1
        d *= c - next((c2 for c2 in range(c-1, -1, -1) if nb[c2, r] >= nb[c, r]), 0)
        d *= next((c2 for c2 in range(c+1, len(nb)) if nb[c2, r] >= nb[c, r]), len(nb)-1) - c
        d *= r - next((r2 for r2 in range(r-1, -1, -1) if nb[c, r2] >= nb[c, r]), 0)
        d *= next((r2 for r2 in range(r+1, len(nb[c])) if nb[c, r2] >= nb[c, r]), len(nb[c])-1) - r
        m = max(m, d)
print(m)