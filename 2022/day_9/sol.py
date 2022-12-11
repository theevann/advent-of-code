import sys
import numpy as np

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    
def do_step(head, tail):
    # If touching, return tail
    if abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1:
        return
    
    if head[0] != tail[0] and head[1] != tail[1]:
        # If not in same row and column, move diagonally
        tail[0] += sign(head[0] - tail[0])
        tail[1] += sign(head[1] - tail[1])
    else:
        # Else move in one direction
        if abs(head[0]-tail[0]) > 1:
            tail[0] += sign(head[0] - tail[0])
        if abs(head[1]-tail[1]) > 1:
            tail[1] += sign(head[1] - tail[1])

moves = {
    "R": (0,1),
    "L": (0,-1),
    "D": (1,0),
    "U": (-1,0)
}

for N in [2, 10]:
    nots = [[500,500] for _ in range(N)]
    grid = np.zeros((1000, 1000), dtype=int)

    for l in data:
        l = l.split()
        dir, dist = l[0], int(l[1])
        
        for _ in range(dist):
            nots[0][0] += moves[dir][0]
            nots[0][1] += moves[dir][1]
            for i in range(1, len(nots)):
                do_step(nots[i-1], nots[i])
            grid[tuple(nots[-1])] = 1

    print(np.sum(grid))