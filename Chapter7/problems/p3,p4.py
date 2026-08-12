from GraphADT import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.scc = []
        self.isolated = []

    def dfs(self):
        #self inherits the function __iter__ from its parent
        for vertex in self:
            if vertex.color == 'white':
                self.dfs_visit(vertex)

        self.transpose()
        self.isolated = self.isolated[::-1]
        
        for vertex in self:
            vertex.color = 'white'

        for vertex in self.isolated:
            if vertex.color == 'white':
                self.scc.append(self.dfs_visit(vertex, True))

            
    def dfs_visit(self, start_vertex, flag=False):
        start_vertex.color = "grey"
        neighbors = start_vertex.get_neighbors()
        self.time += 1
        start_vertex.discovery_time = self.time

        scc = [start_vertex] if flag else None

        for next_vertex in neighbors:
            if next_vertex.color == 'white':
                next_vertex.previous = start_vertex
                result = self.dfs_visit(next_vertex, flag)
                if flag:
                    scc += result

        self.time += 1
        start_vertex.color = 'black'
        start_vertex.closing_time = self.time
        if flag:
            return scc
        
        self.isolated.append(start_vertex)
    
    def print_scc(self):
        for scc in self.scc:
            print(scc)

edges = [
    # SCC {0,1,2,3}
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (1, 3),

    # connection to next SCC
    (2, 4),

    # SCC {4,5}
    (4, 5),
    (5, 4),

    # connection
    (5, 6),

    # SCC {6,7,8}
    (6, 7),
    (7, 8),
    (8, 6),
    (6, 8),

    # connections
    (8, 9),
    (7, 10),

    # SCC {9,10,11}
    (9, 10),
    (10, 11),
    (11, 9),

    # connection
    (11, 12),

    # SCC {12,13}
    (12, 13),
    (13, 12),

    # final SCC
    (13, 14),
    (14, 14)       # SCC {14}
]

g = DFSGraph()
for v1, v2 in edges:
    g.add_edge(v1, v2)
g.dfs()
g.print_scc()