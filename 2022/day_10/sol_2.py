import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()


def do_cycle(cycle, value, X):
    cycle += 1
    value += cycle * X * ((cycle-20) % 40 == 0)
    return cycle, value

X = 1
cycle, value = do_cycle(0, 0, X)
for l in data:
    l = l.split()
    if l[0] == "addx":
        cycle, value = do_cycle(cycle, value, X)
        X += int(l[1])
    cycle, value = do_cycle(cycle, value, X)
print(value)


def do_print(cycle, X):
    cursor = (cycle-1) % 40
    if cursor == 0: print()
    print("@" if X-1 <= cursor <= X+1 else " ", end="")
    return cycle

X = 1
cycle = 1
for l in data:
    do_print(cycle, X)
    l = l.split()
    if l[0] == "addx":
        cycle += 1
        do_print(cycle, X)
        X += int(l[1])
    cycle += 1
print()
    