from GraphADT import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.topological_sort = []
        self.size = 0

    def dfs(self):
        #self inherits the function __iter__ from its parent
        for vertex in self:
            if vertex.color == 'white':
                self.dfs_visit(vertex)

        #we flip the list
        self.topological_sort = self.topological_sort[::-1]


    def dfs_visit(self, start_vertex):
        start_vertex.color = "grey"
        neighbors = start_vertex.get_neighbors()
        self.time += 1
        start_vertex.discovery_time = self.time
        for next_vertex in neighbors:
            if next_vertex.color == 'white':
                next_vertex.previous = start_vertex
                self.dfs_visit(next_vertex)
        self.time += 1
        start_vertex.color = 'black'
        self.topological_sort.append(start_vertex)
        self.size += 1
        start_vertex.closing_time = self.time

    def get_toposort(self):
        return self.topological_sort

def make_graph(g):

    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 5),
        (5, 6)
    ]
    for v1, v2 in edges:
        g.add_edge(v1, v2)

g = DFSGraph()
make_graph(g)
g.dfs()
print(g.get_toposort())