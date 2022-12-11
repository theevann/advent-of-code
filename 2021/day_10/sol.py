import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
    data = [[x for x in y] for y in data]
    

# Part 1
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

total = 0

for line in data:
    current_list = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            current_list.append(c)
        else:
            if c == ")" and current_list[-1] == "(" \
                or c == "]" and current_list[-1] == "[" \
                or c == "}" and current_list[-1] == "{" \
                or c == ">" and current_list[-1] == "<":
                current_list.pop()
            else:
                total += points[c]
                break
                
print(total)


# Part 2
points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

totals = []
for line in data:
    total = 0
    incorrect = False
    current_list = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            current_list.append(c)
        else:
            if c == ")" and current_list[-1] == "(" \
                or c == "]" and current_list[-1] == "[" \
                or c == "}" and current_list[-1] == "{" \
                or c == ">" and current_list[-1] == "<":
                current_list.pop()
            else:
                incorrect = True
                break

    if not incorrect:
        for c in current_list[::-1]:
            total = total*5 + points[c]
        totals.append(total)

print(int(np.median(totals)))
