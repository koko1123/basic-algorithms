"""
Implements Kosaraju's algorithm for finding SCCs on a directed graph
put into an object due to many global variables required for the algorithm
also the most space efficient way I've been able to come up with so far
ydatb
"""
import heapq


# todo memory optimal implementation
# naive implementation: use two separate representations of the graph (reversed and original)
# issue is storing 2n nodes instead of n and 2n book-keeping
# still blazing fast at O(m+n)

class Kosaraju:
    def __init__(self):
        self.ssc_count = heapq.heapify(list())
        self.finishing_times = dict()
        self.finishing_time = 0
        self.graph = dict()
        self.graph_reversed = dict()
        self.leader_nodes = dict()

    def kosaraju_scc_algorithm(self):
        # run dfs loop on the reversed graph and determine the finishing time of each node
        self.first_pass_dfs_loop()
        # run dfs loop on the original graph and determine SSCs  along with size of each
        self.second_pass_dfs_loop()

    # first pass on the reversed graph, use global variables as prescribed
    def first_pass_dfs_loop(self):
        explored = set()
        for node in range(len(self.graph_reversed) - 1, 1, -1):
            if node not in explored:
                self.depth_first_search_first_pass(node, explored)

    def depth_first_search_first_pass(self, node, explored):
        explored.add(node)
        for adjacent_node in self.graph_reversed[node]:
            if adjacent_node not in explored:
                self.depth_first_search_first_pass(adjacent_node, explored)
        self.finishing_time += 1
        self.finishing_times[self.finishing_time] = node

    # second pass on original graph,
    def second_pass_dfs_loop(self):
        explored = set()

    def execute_algorithm(self):
        # input routine
        with open("SCC.txt") as input_file:
            for line in input_file:
                nodes = line.split()
                u = int(nodes[0])
                v = int(nodes[1])

                if u not in self.graph:
                    self.graph[u] = []
                self.graph[u].append(v)

                if v not in self.graph_reversed:
                    self.graph_reversed[v] = []
                self.graph_reversed[v].append(u)


# print lengths of the five largest Strongly Connected Components
kosaraju = Kosaraju()
kosaraju.execute_algorithm()
print(kosaraju.graph_reversed[767009])
