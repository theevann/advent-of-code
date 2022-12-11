import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
    data = [d.split("|") for d in data]
    data = [[d[0].rstrip().split(), d[1].rstrip().split()] for d in data]
    data = [[["".join(sorted(c1)) for c1 in d[0]], ["".join(sorted(c2)) for c2 in d[1]]] for d in data]
# print(data)


# Part 1

cc = 0
for d in data:
    ch = d[1]
    for x in ch:
        if len(x) in [2,3,4,7]:
            cc += 1
print(cc)


# Part 2

tsum = 0
for d in data:
    mapping = [""] * 10
    for c in d[0]+d[1]:
        if c in mapping:
            continue
    
        if len(c) == 2:
            mapping[1] = c
            continue
        elif len(c) == 3:
            mapping[7] = c
            continue
        elif len(c) == 4:
            mapping[4] = c
            continue
        elif len(c) == 7:
            mapping[8] = c
            continue
        
    for c in d[0]+d[1]:
        if c in mapping:
            continue
        
        if len(c) == 5:
            if mapping[7] != "" and set(mapping[7]).issubset(c) or mapping[1] != "" and set(mapping[1]).issubset(c):
                mapping[3] = c
                continue
                
            if (mapping[1] != "" and not set(mapping[1]).issubset(c)) or (mapping[7] != "" and not set(mapping[7]).issubset(c)):
                if mapping[1] != "" and mapping[4] != "":
                    if set(mapping[4]).difference(set(mapping[1])).issubset(c):
                        mapping[5] = c
                        continue
                    else:
                        mapping[2] = c
                        continue
        elif len(c) == 6:
            if mapping[1] != "" and not set(mapping[1]).issubset(c):
                mapping[6] = c
                continue
            
            if mapping[4] != "" and set(mapping[4]).issubset(c):
                mapping[9] = c
                continue
            
            if mapping[4] != "" and not set(mapping[4]).issubset(c):
                if mapping[1] != "" and set(mapping[1]).issubset(c):
                    mapping[0] = c
                    continue
        
    psum = 0
    for number in d[1]:
        rnumber = mapping.index(number)
        psum = psum*10 + rnumber
    tsum += psum
print(tsum)