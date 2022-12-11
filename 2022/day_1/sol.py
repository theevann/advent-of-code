import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()

# print(sorted(sum(ints(x)) for x in data.replace("\n", " ").split("  "))[-1])
# print(sum(sorted(sum(ints(x)) for x in data.replace("\n", " ").split("  "))[-3:]))

sum_list = []
cs = 0
for x in data:
    if x == '':
        sum_list.append(cs)
        cs = 0
    else:
        cs += int(x)
sum_list = sorted(sum_list)

print(sum_list[-1])
print(sum(sorted(sum_list)[-3:]))