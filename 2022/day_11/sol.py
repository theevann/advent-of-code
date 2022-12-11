import sys, re
from functools import reduce


def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))


in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()


def parse_data(data):
    i = 1
    monkeys = []
    while i < len(data):
        monkey = []
        l = data[i]
        monkey += [list(ints(l))]
        
        l = data[i+1].split()
        monkey += [l[-2:]]
        
        l = data[i+2].split()
        monkey += [int(l[-1])]
        
        l = data[i+3].split()
        monkey += [int(l[-1])]
        
        l = data[i+4].split()
        monkey += [int(l[-1])]
        
        i += 7
        monkeys += [monkey]
    return monkeys
    

def update_worry(worry, ops, part):
    op, value = ops
    value = worry if value == "old" else int(value)
    worry = worry * value if op == "*" else worry + value
    return worry // 3 if part == 1 else worry % common_multiple


for part, n_rounds in zip([1, 2], [20, 10000]):
    monkeys = parse_data(data)
    common_multiple = reduce(lambda a,b: a*b[2], monkeys, 1)
    n_inspects = [0] * len(monkeys)
    for round in range(n_rounds):
        for i, monkey in enumerate(monkeys):
            worries, ops, cond, to_true, to_false = monkey
            n_inspects[i] += len(worries)
            for worry in worries[:]:
                monkey[0].remove(worry)
                worry = update_worry(worry, ops, part)
                to_monkey = to_true if worry % cond == 0 else to_false
                monkeys[to_monkey][0] += [worry]

    a, b = sorted(n_inspects)[-2:]
    print(a*b)
