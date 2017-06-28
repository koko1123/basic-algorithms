"""
Heap based implementation of Dijkstra's Algorithm
"""

# assumes starting point is always node 1
import queue


def dijkstra_algorithm(graph, target):
    dijkstra_heap = queue.PriorityQueue()
    dijkstra_heap.put((0, 1))
    visited = set()
    while not dijkstra_heap.empty():
        current = dijkstra_heap.get()
        current_node = current[1]
        visited.add(current_node)
        distance = current[0]
        if current_node == target:
            return current[0]
        else:
            for adj_node in range(len(graph)):
                if adj_node not in visited and current_node != adj_node and graph[current_node][adj_node] != 0:
                    dijkstra_heap.put((distance + graph[current_node][adj_node], adj_node))
    # couldn't find the target
    return -1


# input routine
with open('dijkstraData.txt') as input_file:
    num_elements = 200
    input_graph = [[0 for x in range(201)] for y in range(201)]
    for lines in input_file:
        elements = lines.split()
        node = int(elements[0])
        for element in range(1, len(elements)):
            values = elements[element].split(',')
            index = int(values[0])
            if input_graph[node][index] == 0:
                input_graph[node][index] = int(values[1])

    targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for target_value in targets:
        print(str(dijkstra_algorithm(input_graph, target_value)) + ',')
