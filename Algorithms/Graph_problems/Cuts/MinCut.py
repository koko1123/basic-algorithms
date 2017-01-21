import random
"""
Implementation of Karger's MinCut Algorithm
the input is an adjacency list of the format
x (node ) followed by n nodes adjacent to it
Example:
    1 2 3 4
    2 4 1
    3 4 1
    4 3 2 1
represents a square with vertices numbered clockwise
the square has a diagonal edge (1,4)
"""


def karger_algorithm(adjacency_list):
    while len(adjacency_list) > 2:
        random_u = random.choice(adjacency_list.keys())
        random_v = random.choice(adjacency_list[random_u])
        contraction(random_u, random_v, adjacency_list)
    return len(adjacency_list[list(adjacency_list.keys())[0]])


def contraction(u, v, adjacency_list):
    for adjacent_node in u:
        if adjacent_node != v:
            adjacency_list[v].append(adjacent_node)
            adjacency_list[adjacent_node].append(v)
        adjacency_list[adjacency_node].remove(u)
    adjacency_list.remove(u)



