import sys, re
import numpy as np

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

def floats(inp: str = None):
    return map(float, re.findall(r"-?\d+(?:\.\d*)?", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()

ops = np.zeros(len(data)*2)
ops[0] = 1
cycle = 0
for i, l in enumerate(data):
    l = l.split()
    if l[0] == "addx":
        ops[cycle + 2] += int(l[1])
        cycle += 1
    cycle += 1

X = ops.cumsum()
sm = (X[19:cycle:40] * np.arange(20, cycle, 40)).sum()
print(int(sm))


for i in range(cycle):
    cursor = i % 40
    
    if cursor == 0:
        print("")
    if X[i]-1 <= cursor <= X[i]+1:
        print("@", end="")
    else:
        print(" ", end="")
        # if (v+1) % 5 == 0:
        #     print("   ", end="")
print()
        
    