import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    
s = 0
for d in data:
    a, b = d.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    if int(a1) <= int(b1) and int(b2) <= int(a2):
        s += 1
    elif int(b1) <= int(a1) and int(a2) <= int(b2):
        s += 1
print(s)

s = 0
for d in data:
    a, b = d.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    if int(a2) >= int(b1) and int(a1) <= int(b2):
        s += 1
print(s)