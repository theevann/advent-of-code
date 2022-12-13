import sys
from functools import cmp_to_key


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()
    

def check_order(a, b):
    in_order = None
    
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            in_order = False
        elif a < b:
            in_order = True
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if i >= len(b):
                in_order = False
                break
            in_order = check_order(a[i], b[i])
            if in_order is not None:
                break
        else:
            in_order = True if len(a) < len(b) else None 
    elif isinstance(a, list) and isinstance(b, int):
        in_order = check_order(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        in_order = check_order([a], b)

    return in_order

# Part 1
sum_indices = 0
for i in range(0, len(data), 3):
    a = eval(data[i])
    b = eval(data[i+1])
    if check_order(a, b) != False:
        sum_indices += i // 3 + 1
print(sum_indices)


# Part 2
data = [eval(i) for i in data if i != ''] + [[[2]], [[6]]]
data = sorted(data, key=cmp_to_key(lambda a,b: -1 if check_order(a,b) == False else 1), reverse=True)
    
id_1 = data.index([[2]]) + 1
id_2 = data.index([[6]]) + 1
print(id_1 * id_2)