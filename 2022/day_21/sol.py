import sys, re
from functools import reduce

AMIN = -float("inf")
AMAX = float("inf")
sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)
prod = lambda array: reduce(lambda a, b: a * b, array, 1)

def ints(inp: str = None):
    return map(int, re.findall(r"-?\d+", inp or sys.stdin.read()))

def floats(inp: str = None):
    return map(float, re.findall(r"-?\d+(?:\.\d*)?", inp or sys.stdin.read()))

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()
    
class Monkey():
    def __init__(self, name) -> None:
        self.name = name
        self.value = None
        self.instr = None
    
    def __repr__(self) -> str:
        return f"{self.name} {self.value} {self.instr}"

def read_data(data):   
    monkeys = {} 
    for l in data:
        a,b = l.split(": ")
        mk = Monkey(a) if a not in monkeys else monkeys[a]
        monkeys[a] = mk
        if b.isdigit():
            mk.value = int(b)
        else:
            instr = b.split(" ")
            mk.instr = instr
    return monkeys


def make_op(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return int(a / b)


# Part 1
def get_value(mk, monkeys):
    if mk.value is not None:
        return mk.value
    
    mk1 = get_value(monkeys[mk.instr[0]], monkeys)
    mk2 = get_value(monkeys[mk.instr[2]], monkeys)
    
    mk.value = make_op(mk1, mk2, mk.instr[1])
        
    return mk.value

monkeys = read_data(data)
print(get_value(monkeys["root"], monkeys))


# Part 2

# With backward computation using string manipulation
def get_ops(mk, monkeys):
    if mk.name == "humn":
        return mk.name
    
    if mk.value is not None:
        return mk.value
    
    mk1 = get_ops(monkeys[mk.instr[0]], monkeys)
    mk2 = get_ops(monkeys[mk.instr[2]], monkeys)
    
    if isinstance(mk1, int) and isinstance(mk2, int):
        mk.value = make_op(mk1, mk2, mk.instr[1])
    else:
        mk.value = (mk1, mk.instr[1], mk2)
        
    return mk.value

monkeys = read_data(data)
root = monkeys["root"]
a = get_ops(monkeys[root.instr[0]], monkeys)
b = get_ops(monkeys[root.instr[2]], monkeys)

a, b = (b, a) if isinstance(b, int) else (a, b)
value, instr = a, b

while instr != "humn":
    # print(instr)
    a, ins, b = instr
    
    if isinstance(a, int):
        instr = b

        if ins == "+":
            value -= a
        elif ins == "-":
            value = a - value
        elif ins == "*":
            value /= a
        elif ins == "/":
            value = a / value
        
    else:
        instr = a
        
        if ins == "+":
            value -= b
        elif ins == "-":
            value += b
        elif ins == "*":
            value /= b
        elif ins == "/":
            value *= b

print(int(value))


# With binary search
def get_repr(mk, monkeys):
    if mk.name == "humn":
        return mk.name
    
    if mk.value is not None:
        return mk.value
    
    mk1 = get_repr(monkeys[mk.instr[0]], monkeys)
    mk2 = get_repr(monkeys[mk.instr[2]], monkeys)
    
    if isinstance(mk1, int) and isinstance(mk2, int):
        mk.value = make_op(mk1, mk2, mk.instr[1])
    else:
        mk.value = f"({mk1} {mk.instr[1]} {mk2})"
        
    return mk.value

monkeys = read_data(data)
root = monkeys["root"]
a = get_repr(monkeys[root.instr[0]], monkeys)
b = get_repr(monkeys[root.instr[2]], monkeys)

a, b = (b, a) if isinstance(b, int) else (a, b)
value, instr = a, b

s = sign(eval(instr.replace("humn", str(1))) - eval(instr.replace("humn", str(0))))

mn, mx = 0, 1e15
while mn < mx:
    val = int((mn + mx) // 2)
    diff = value - eval(instr.replace("humn", str(val)))
    if diff*s > 0:
        mn = val + 1
    else:
        mx = val
print(mn)

