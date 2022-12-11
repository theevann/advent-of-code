import sys
import json
import copy
from dataclasses import dataclass

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    ordata = f.read().splitlines()
ordata = [json.loads(x) for x in ordata]


# Wrapper class needed for reference
@dataclass(order=True)
class Wrapper():
    value: int
    
    def __repr__(self):
        return str(self.value)

def int2Wrapper(arr):
    return [int2Wrapper(x) if type(x) == list else Wrapper(x) for x in arr]
    


def get_prev_left(x):
    return get_prev_left(x[1]) if type(x) == list else x
    
def get_next_right(x):
    return get_next_right(x[0]) if type(x) == list else x

def is_snail(arr):
    return type(arr[0]) == type(arr[1]) == Wrapper

def explode(arr, deep=1, prev_left=None, last_right=None):
    for i, x in enumerate(arr):
        if type(x) != list: continue
        prev_left = get_prev_left(arr[i-1]) if i > 0 else prev_left
        next_right = get_next_right(arr[i+1]) if i < len(arr)-1 else last_right

        if deep >= 4 and is_snail(x):
            if prev_left is not None:
                prev_left.value += x[0].value
            if next_right is not None:
                next_right.value += x[1].value
            arr[i] = Wrapper(0)
            return True
        else:
            out = explode(x, deep+1, prev_left, next_right)
            if out:
                return True
    return False

def split(arr):
    for i, x in enumerate(arr):
        if type(x) == list:
            if split(x):
                return True
        elif x >= Wrapper(10):
            arr[i] = [Wrapper(x.value//2), Wrapper((x.value+1)//2)]
            return True
    return False

def add_snail_numbers(arr1, arr2):
    result = [arr1] + [arr2]
    action = True
    while action:
        action = explode(result) or split(result)
    return result

def magnitude(arr):
    if type(arr) == Wrapper:
        return arr.value
    return 3*magnitude(arr[0]) + 2*magnitude(arr[1])


# Part 1
data = int2Wrapper(ordata)

result = data[0]
for line in data[1:]:
    result = add_snail_numbers(result, line)
print(magnitude(result))


# Part 2
data = int2Wrapper(ordata)

max_magn = 0
for i in range(len(data)):
    for j in range(len(data)):
        if i != j:
            result = add_snail_numbers(copy.deepcopy(data[i]), copy.deepcopy(data[j]))
            max_magn = max(max_magn, magnitude(result))
print(max_magn)

