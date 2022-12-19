import sys, re
from functools import reduce
from copy import deepcopy
from math import ceil

prod = lambda array: reduce(lambda a, b: a * b, array, 1)

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()
    
data = [list(ints(y)) for y in data]

def get_rsrc_after(rsrcs, robots, time):
    new_rsrc = deepcopy(rsrcs)
    for i in range(4):
        new_rsrc[i] += robots[i] * time
    return new_rsrc

def compute_geodes(bp, time, robots, resources, max_time, max_so_far=0):
    mx = 0
    
    # If max_so_far is bigger than upper bound on the number of geodes we can make
    if max_so_far > get_rsrc_after(resources, robots, max_time-time+1)[-1] + (max_time - time + 1)**2 / 2:
        return 0
    
    # if making an ore robot
    time_needed = 1 + (max(ceil((bp[1] - resources[0]) / robots[0]), 0))
    mx0 = max(bp[i] for i in [1,2,3,5])
    if time_needed + time <= max_time and robots[0] < mx0:# and resources[0] < mx0*2:
        new_rsrc = get_rsrc_after(resources, robots, time_needed)
        new_rsrc[0] -= bp[1]
        robots[0] += 1
        v = compute_geodes(bp, time+time_needed, robots, new_rsrc, max_time, max_so_far)
        robots[0] -= 1
        mx = max(mx, v)
        max_so_far = max(max_so_far, mx)

    # if making a clay robot
    time_needed = 1 + (max(ceil((bp[2] - resources[0]) / robots[0]), 0))
    if time_needed + time <= max_time and robots[1] < bp[4]:# and resources[1] < bp[4]:
        new_rsrc = get_rsrc_after(resources, robots, time_needed)
        new_rsrc[0] -= bp[2]
        robots[1] += 1
        v = compute_geodes(bp, time+time_needed, robots, new_rsrc, max_time, max_so_far)
        robots[1] -= 1
        mx = max(mx, v)
        max_so_far = max(max_so_far, mx)
    
    # if making an obsidian robot
    if robots[1] > 0:
        time_needed = 1 + (max(
            ceil((bp[3] - resources[0]) / robots[0]),
            ceil((bp[4] - resources[1]) / robots[1]),
            0))
        if resources[2] + (max_time+1-time) * robots[2] + (max_time-time_needed) >= bp[6]:
        
            if time_needed + time <= max_time:
                new_rsrc = get_rsrc_after(resources, robots, time_needed)
                new_rsrc[0] -= bp[3]
                new_rsrc[1] -= bp[4]
                robots[2] += 1
                v = compute_geodes(bp, time+time_needed, robots, new_rsrc, max_time, max_so_far)
                robots[2] -= 1
                mx = max(mx, v)
                max_so_far = max(max_so_far, mx)
    
    # if making a geode robot
    if robots[2] > 0:
        time_needed = 1 + (max(
            ceil((bp[5] - resources[0]) / robots[0]),
            ceil((bp[6] - resources[2]) / robots[2]),
            0))
        
        if time_needed + time <= max_time:
            new_rsrc = get_rsrc_after(resources, robots, time_needed)
            new_rsrc[0] -= bp[5]
            new_rsrc[2] -= bp[6]
            robots[3] += 1
            v = compute_geodes(bp, time+time_needed, robots, new_rsrc, max_time, max_so_far)
            robots[3] -= 1
            mx = max(mx, v)
    
    # if making no new robots
    v = get_rsrc_after(resources, robots, max_time+1-time)[-1]
    mx = max(mx, v)
    
    # if time < 10:
    #     print(time, robots, resources, mx, max_so_far)
    
    return mx


s = sum(bp_id*compute_geodes(bp, 1, [1,0,0,0], [0,0,0,0], 24) for bp_id, bp in enumerate(data, 1))
print(s)

p = prod(compute_geodes(bp, 1, [1,0,0,0], [0,0,0,0], 32) for bp in data[:3])
print(p)