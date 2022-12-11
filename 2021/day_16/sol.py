import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
    # data = [[int(x) for x in y.split()] for y in data]
# data = np.loadtxt("input", dtype=int, delimiter="\n")

bs = str(bin(int(data[0], 16)))[2:]
sum_version = 0
size = len(data[0])*4
bs = "0" * (size - len(bs)) + bs



# Part 1 & 2
def parse_litteral(bst):
    repres = ""
    cont = True
    while cont:
        cont = bst[0] != "0"
        repres += bst[1:5]
        bst = bst[5:]
    return bst, int(repres, 2)
        

def decode_packet(bst, max_sub=100000):
    global sum_version
    
    values = []
    sum_sub = 0
    while len(bst) > 0 and int(bst) != 0 and sum_sub < max_sub:
        sum_sub += 1
        version = int(bst[:3], 2)
        type = int(bst[3:6], 2)
        sum_version += version
        
        if type == 4:
            bst, vls = parse_litteral(bst[6:])
        else:
            length_type = int(bst[6], 2)
            if length_type == 0:
                length = int(bst[7:22], 2)
                _, vls = decode_packet(bst[22:22+length])
                bst = bst[22+length:]
            elif length_type == 1:
                n_sub = int(bst[7:18], 2)
                bst, vls = decode_packet(bst[18:], max_sub=n_sub)
        values += [reduction[type](vls)]
                
    return bst, values


reduction = {
    0: sum,
    1: np.prod,
    2: np.min,
    3: np.max,
    4: lambda x: x,
    5: lambda arr: 1 if arr[0] > arr[1] else 0, 
    6: lambda arr: 1 if arr[0] < arr[1] else 0,  
    7: lambda arr: 1 if arr[0] == arr[1] else 0,  
}


_, [result] = decode_packet(bs)
print(sum_version)
print(result)


# Further

def packet2json(bst, max_sub=100000):   
    sum_sub = 0
    content = []
    while len(bst) > 0 and int(bst) != 0 and sum_sub < max_sub:
        sum_sub += 1
        version = int(bst[:3], 2)
        type = int(bst[3:6], 2)
        
        if type == 4:
            bst, ctt = parse_type_4(bst[6:])
            ctt = ctt
        else:
            length_type = int(bst[6], 2)
            if length_type == 0:
                length = int(bst[7:22], 2)
                _, ctt = packet2json(bst[22:22+length])
                bst = bst[22+length:]
            elif length_type == 1:
                n_sub = int(bst[7:18], 2)
                bst, ctt = packet2json(bst[18:], max_sub=n_sub)
        content += [{
            "type": type,
            "version": version,
            "content": ctt
        }]
            
    return bst, content


import json
obj = packet2json(bs)[1]
# print(json.dumps(obj, indent=2))