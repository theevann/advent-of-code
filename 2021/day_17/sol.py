import sys
in_file = sys.argv[1] if len(sys.argv) > 1 else "input"

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

with open(in_file, 'r') as f:
    data = f.read().splitlines()
data = [[int(x) for x in y.split(",")] for y in data]
x0, x1 = data[0]
y0, y1 = data[1]


# Part 1 and 2
def simulate(vx, vy):
    max_y = AMIN
    was_in = False
    x,y = 0,0
    while x <= x1 and y >= y0:
        x += vx
        y += vy
        vx -= sign(vx)
        vy -= 1
        max_y = max(max_y, y)
        
        if (x0 <= x <= x1) and (y0 <= y <= y1):
            was_in = True
            break
    return max_y if was_in else None


max_vx = None
max_vy = None
max_y = AMIN
sum_velocities = 0
for vx in range(0, 300):  # As our x1 == 283
    for vy in range(-200, 500):  # As our y0 == -107
        highest_y = simulate(vx, vy)
        if highest_y is not None:
            sum_velocities += 1
            if highest_y > max_y:
                max_y = highest_y
                max_vx = vx
                max_vy = vy

print(max_y)
print(sum_velocities)