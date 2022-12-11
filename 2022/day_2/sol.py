import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    
shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win_score = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}  

score = 0
for l in data:
    x, y = l.split(" ")
    score += shape_score[y]
    score += win_score[x][y]
print(score)


win_score = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

shape_score = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}

score = 0
for l in data:
    x, y = l.split(" ")
    score += shape_score[x][y]
    score += win_score[y]
print(score)