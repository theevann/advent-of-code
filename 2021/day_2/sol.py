import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()

# Part 1
H = 0
D = 0
for d in data:
    cmd, x = d.split(' ')
    x = int(x)
    
    if cmd == "forward":
        H += x
    elif cmd == "down": 
        D += x
    elif cmd == "up":
        D -= x
        
print(D*H)


# Part 2
H = 0
D = 0
A = 0
for d in data:
    cmd, x = d.split(' ')
    x = int(x)
    
    if cmd == "forward":
        H += x
        D += A*x
    elif cmd == "down": 
        A += x
    elif cmd == "up":
        A -= x
        
print(D*H)