"""
Fast implementation of Prim's algorithm with a heap (very similar of djikstra's) 
"""
import Queue


# run Prim's algorithm and return the cost of the MST
def prims_algorithm(graph):
    unvisited_node = {x for x in range(1, len(graph))}
    # start with 0
    start_node = (0, 0)
    edge_heap = Queue.PriorityQueue()
    mst_edge_cost = 0
    edge_heap.put(start_node)
    while len(unvisited_node) > 0:
        current_node = edge_heap.get()
        current_node_num = current_node[1]
        for adj_node in range(len(graph[current_node_num])):
            node_distance = graph[current_node_num][adj_node]
            if node_distance > 0 and adj_node in unvisited_node:
                unvisited_node.remove(adj_node)
                edge_heap.put((node_distance, adj_node))
        mst_edge_cost += current_node[0]
    return mst_edge_cost


# input for graph
def input_routine():
    return "input"


# print BFS traversal of the graph
def print_graph(graph):
    print(graph)


graph = input_routine()
print_graph(prims_algorithm(graph))
