import sys
from collections import Counter
from functools import lru_cache
from itertools import cycle

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
p1, p2 = open(in_file).read().splitlines()

init_pos_1 = int(p1[-1])
init_pos_2 = int(p2[-1])


# Part 1
scores = [0, 0]
pos = [init_pos_1, init_pos_2]
dice = cycle(range(1, 101))
turn = 0

def player_pos(p):
    return (p-1) % 10 + 1

while max(scores) < 1000:
    pos[turn%2] = player_pos(pos[turn%2] + next(dice) + next(dice) + next(dice))
    scores[turn%2] += pos[turn%2]
    turn += 1
print(min(scores) * 3 * turn)


# Part 2
array = Counter([i+j+k for i in range(1,4) for j in range(1,4) for k in range(1,4)])

@lru_cache(None)
def play(s1, p1, s2, p2):
    wins1, wins2 = 0, 0
    for value, qtt in array.items():
        new_pos = player_pos(p1+value)
        if s1 + new_pos >= 21:
            wins1 += qtt
        else:
            win2, win1 = play(s2, p2, s1+new_pos, new_pos)
            wins1 += qtt * win1
            wins2 += qtt * win2
    return wins1, wins2

print(max(play(0, init_pos_1, 0, init_pos_2)))
print(play.cache_info())