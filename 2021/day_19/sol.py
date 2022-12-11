import sys
import numpy as np
from collections import Counter, defaultdict

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()

scanner = -1
scanner_data = []
for line in data:
    if "scanner" in line.split():
        scanner += 1
        scanner_data.append([])
    elif line != "":
        scanner_data[scanner] += [[int(x) for x in line.split(",")]]

scanner_data = [np.array(line) for line in scanner_data]
num_scanner = len(scanner_data)


mutual_dist = []
for sc in scanner_data:
    sc_mutual = []
    for line in sc:
        # sc_mutual += [set(((sc - line)**2).sum(1))]
        sc_mutual += [Counter(((sc - line)**2).sum(1))]
    mutual_dist += [sc_mutual]



# all_beacon = set()
# for i, sc in enumerate(scanner_data):
#     for j in range(len(sc)):
#         all_beacon.add((i, j))

# for i in range(scanner+1):
#     for j in range(i+1, scanner+1):
#         for idi, d0s in enumerate(mutual_dist[i]):
#             for idj, d1s in enumerate(mutual_dist[j]):
#                 if len(d0s.intersection(d1s)) > 2:
#                     if (j, idj) in all_beacon:
#                         all_beacon.remove((j, idj))
# print(len(all_beacon))



scanner_positions = {0: [0,0,0]}
scanner_mapaxes = {0: [0,1,2]}
scanner_orientations = {0: [1,1,1]}
common_beacons = defaultdict(set)

while len(scanner_positions) < num_scanner:
    for i in range(num_scanner):
        for j in range(i+1, num_scanner):
            for idi, d0s in enumerate(mutual_dist[i]):
                for idj, d1s in enumerate(mutual_dist[j]):
                    
                    # if len(d0s.intersection(d1s)) < 12:
                    if sum((d0s & d1s).values()) < 12:
                        continue
                    common_beacons[(i,j)].add((idi, idj))
                    
                    
                    if len(common_beacons[(i,j)]) > 1:
                        if (i in scanner_positions) and (j not in scanner_positions):
                            ii, jj = i, j
                            swap = 0
                        elif (j in scanner_positions) and (i not in scanner_positions):
                            ii, jj = j, i
                            swap = 1
                        else:
                            continue
                            
                        cur_common = list(common_beacons[(i,j)])
                        b00_id, b10_id = cur_common[0] if not swap else cur_common[0][::-1]
                        b01_id, b11_id = cur_common[1] if not swap else cur_common[1][::-1]
                        
                        b00 = scanner_data[ii][b00_id]
                        b01 = scanner_data[ii][b01_id]
                        b10 = scanner_data[jj][b10_id]
                        b11 = scanner_data[jj][b11_id]
                        
                        s_pos = scanner_positions[ii]
                        s_map = scanner_mapaxes[ii]
                        s_ort = scanner_orientations[ii]
                        
                        ort = [None] * 3
                        mapaxis = [None] * 3
                        for k in range(3):
                            dx = (b00[s_map[k]] - b01[s_map[k]])*s_ort[k]
                            for l in range(3):
                                for v in [-1, 1]:
                                    if (b10[l] - b11[l])*v == dx:
                                        mapaxis[k] = l
                                        ort[k] = v
                        
                        pos = [s_pos[x] + b01[s_map[x]]*s_ort[x] - b11[mapaxis[x]]*ort[x] for x in range(3)]

                        scanner_positions[jj] = pos
                        scanner_orientations[jj] = ort
                        scanner_mapaxes[jj] = mapaxis


# Part 1
all_beacon = set()
for scanner_id in range(num_scanner):
    for beacon in scanner_data[scanner_id]:
        new_pos = [scanner_positions[scanner_id][i] + beacon[scanner_mapaxes[scanner_id][i]]*scanner_orientations[scanner_id][i] for i in range(3)]
        all_beacon.add(tuple(new_pos))
print(len(all_beacon))


# Part 2
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

max_man = 0
for s1 in scanner_positions.values():
    for s2 in scanner_positions.values():
        max_man = max(max_man, manhattan_distance(s1, s2))
print(max_man)



# Potential flaws of this implementation:
# If some scanners are at the same spot...
# Then the detection will partly fail,
# with mapaxis variable containing the same value