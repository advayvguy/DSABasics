from GraphADT import Graph, Queue

class BFSGrpah(Graph):
    def __init__(self):
        super().__init__()
        self.vertex_pairs = {}

    def bfs(self, v):
        queue = Queue()
        queue.enqueue(v)
        while queue.size() > 0:
            vertex = queue.dequeue()
            for next_vertex in vertex.get_neighbors():
                if next_vertex.color == 'white':
                    next_vertex.color = 'grey'
                    queue.enqueue(next_vertex)
                    next_vertex.distance = vertex.distance + 1
            vertex.color = 'black'

    def all_distance(self):
        for current in self:
            for v in self:
                v.distance = 0
            
            self.bfs(current)

            for v in self:
                if v != current and v.color == 'black':
                    self.vertex_pairs[(current, v)] = v.distance
            
            for v in self:
                v.distance = 0
                v.color = 'white'
        
        for (v, v_next), distance in self.vertex_pairs.items():
                if distance > 0:
                    print(f"{v.get_key(), v_next.get_key()} -> {distance}")

def create_graph():
    graph = BFSGrpah()

    edge_list = [
        (0, 1, 0), (1, 0, 0),
        (0, 2, 0), (2, 0, 0),
        (1, 2, 0), (2, 1, 0),
        (1, 3, 0), (3, 1, 0),
        (2, 4, 0), (4, 2, 0),
        (3, 4, 0), (4, 3, 0)
    ]

    graph.add_edges(edge_list)

    return graph

g = create_graph()
g.all_distance()