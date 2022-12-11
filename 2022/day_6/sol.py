import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()[0]
    

for j in [4,14]:
    for i in range(len(data)):
        if len(set(data[i:i+j])) == j:
            print(i+j)
            break