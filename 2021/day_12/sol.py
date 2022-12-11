import numpy as np


with open('input', 'r') as f:
    data = f.read().splitlines()
    data = [[x for x in y.split("-")] for y in data]


neighbours = {}
for l in data:
    if l[0] not in neighbours:
        neighbours[l[0]] = set([l[1]])
    else:
        neighbours[l[0]].add(l[1])
    if l[1] not in neighbours:
        neighbours[l[1]] = set([l[0]])
    else:
        neighbours[l[1]].add(l[0])


def is_small(node):
    return node != node.upper()

def visit(node, full_path, small_visited, visited_twice):
    if node == "end":
        visited_paths.add(tuple(full_path + ["end"]))
        return

    full_path = full_path + [node]
    for neigh_node in neighbours[node]:
        if neigh_node not in small_visited:
            if is_small(node):
                visit(neigh_node, full_path, small_visited + [node], visited_twice)
                if not visited_twice and node != "start":
                    visit(neigh_node, full_path, small_visited, True)
            else:
                visit(neigh_node, full_path, small_visited, visited_twice)


# Part 1
visited_paths = set()
visit("start", [], [], True)
print(len(visited_paths))

# Part 2
visited_paths = set()
visit("start", [], [], False)
print(len(visited_paths))
   