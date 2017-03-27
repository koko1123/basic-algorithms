"""
Implements Kosaraju's algorithm for finding SCCs on a directed graph
put into an object due to many global variables required for the algorithm
also the most space efficient way I've been able to come up with so far
ydatb
"""


# todo memory optimal implementation
# naive implementation: use two separate representations of the graph (reversed and original)
# issue is storing 2n nodes instead of n and 2n book-keeping
# still blazing fast at O(m+n)
# yes, I know this is dangerous


class Kosaraju:
    def __init__(self):
        self.ssc_count = list()
        self.finishing_times = dict()
        self.finishing_time = 0
        self.graph = dict()
        self.graph_reversed = dict()
        self.leader_nodes = dict()
        self.explored = set()
        # since nodes are labelled 1-n, 0 is a safe placeholder value
        self.source = 0

    def kosaraju_scc_algorithm(self):
        # run dfs loop on the reversed graph and determine the finishing time of each node
        self.first_pass_dfs_loop()
        # run dfs loop on the original graph and determine SSCs  along with size of each
        self.second_pass_dfs_loop()

    # first pass on the reversed graph, use global variables as prescribed
    def first_pass_dfs_loop(self):
        self.explored = set()
        for node in range(len(self.graph_reversed) - 1, 0, -1):
            if node not in self.explored:
                self.depth_first_search_first_pass(node)

    def depth_first_search_first_pass(self, node):
        self.explored.add(node)
        for adjacent_node in self.graph_reversed[node]:
            if adjacent_node not in self.explored:
                self.depth_first_search_first_pass(adjacent_node)
        self.finishing_time += 1
        self.finishing_times[self.finishing_time] = node

    # second pass on original graph this time associate nodes with leader
    # also traverse according to finishing times (decreasing order)
    def second_pass_dfs_loop(self):
        self.explored = set()
        # every node has exactly one finishing time in the range 1 to n
        # also largest finishing time is n
        for f_value in range(len(self.finishing_times) - 1, 0, -1):
            node = self.finishing_times[f_value]
            if node not in self.explored:
                self.source = node
                self.depth_first_search_second_pass(node)

    # second pass DFS on original graph
    def depth_first_search_second_pass(self, node):
        self.explored.add(node)
        if self.source not in self.leader_nodes:
            self.leader_nodes[self.source] = []
        self.leader_nodes[self.source].append(node)
        for adjacent_node in self.graph[node]:
            if adjacent_node not in self.explored:
                self.depth_first_search_second_pass(adjacent_node)

    def input_routine(self):
        # input routine
        with open("SCC.txt") as input_file:
            for line in input_file:
                nodes = line.split()
                u = int(nodes[0])
                v = int(nodes[1])

                if u not in self.graph:
                    self.graph[u] = set()
                if v not in self.graph:
                    self.graph[v] = set()
                if v != u:
                    self.graph[u].add(v)

                if v not in self.graph_reversed:
                    self.graph_reversed[v] = set()
                if u not in self.graph_reversed:
                    self.graph_reversed[u] = set()
                if v != u:
                    self.graph_reversed[v].add(u)

    def execute_algorithm(self):
        self.input_routine()
        self.kosaraju_scc_algorithm()
        for key in self.leader_nodes:
            self.ssc_count.append(len(self.leader_nodes[key]))
        self.ssc_count.sort(key=lambda x: -x)
