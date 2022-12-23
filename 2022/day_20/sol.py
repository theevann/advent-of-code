import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
data = open(in_file, 'r').read().splitlines()

def solve(data, round, decryption_key):
    data = [(i, int(y)*decryption_key) for i, y in enumerate(data)]

    mixed_data = data[:]
    for _ in range(round):
        for d in data:
            if d[1] == 0:
                continue
            to_move = d[1] % (len(data)-1)
            to_move = to_move-1 if to_move < 0 else to_move
            current_idx = mixed_data.index(d)
            obj_before = mixed_data[(current_idx + to_move) % len(data)]
            mixed_data.remove(d)
            to_go_idx = mixed_data.index(obj_before)
            mixed_data.insert(to_go_idx + 1, d)
        
    index_0 = mixed_data.index(next(d for d in mixed_data if d[1] == 0))
    print(sum(mixed_data[(index_0 + 1000*k) % len(data)][1] for k in range(1, 4)))

solve(data, 1, 1)
solve(data, 10, 811589153)