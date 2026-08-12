from GraphADT import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        #self inherits the function __iter__ from its parent
        for vertex in self:
            if vertex.color == 'white':
                self.dfs_visit(vertex)
        
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
        start_vertex.closing_time = self.time