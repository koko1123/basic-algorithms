import random
import copy
"""
Implementation of Karger's MinCut Algorithm
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


def read_graph():
    file = open('kargerMinCut.txt', 'r')
    adjacency_graph = {}
    for line in file:
        node = int(line.split()[0])
        adjacent_nodes = [int(x) for x in line.split()[1:]]
        adjacency_graph[node] = adjacent_nodes
    return adjacency_graph


graph = read_graph()
print(graph)

