import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()

def score(l):
    if l.isupper():
        return ord(l) - ord('A') + 27
    else:
        return ord(l) - ord('a') + 1

s = 0
for d in data:
    l = list(set(d[:len(d)//2]).intersection(set(d[len(d)//2:])))[0]
    s += score(l)
print(s)

s = 0
for i in range(0, len(data), 3):
    l = list(set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2])))[0]
    s += score(l)
print(s)