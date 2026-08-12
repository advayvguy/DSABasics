from general_dfs import DFSGraph

def transpose(g):
    edges = []
    for vertex in g.vertices.values():
        for neighbor in vertex.get_neighbors():
            edges.append((vertex.get_key(), neighbor.get_key())) #if we change the neighbor while traversing we lose the path
    
    for from_vertex, to_vertex in edges:
        g.flip_edge(from_vertex, to_vertex)

def scc(g):
    g.dfs()
    transpose(g)
    for vertex in g:
        vertex.color = 'white'
    vertices = list(g.vertices.values())
    vertices.sort(key= lambda vertex: vertex.closing_time, reverse=True)
    for vertex in vertices:
        if vertex.color == 'white':
            g.dfs_visit(vertex)
        else:
            continue
        #if the function breaks: it cycled back, we have to print out the vertices which are black
        scc_list = []
        for vertex in g:
            if vertex.color == 'black':
                vertex.color = 'black'
                scc_list.append(vertex)
        print(scc_list)

graph = DFSGraph()
graph2 = DFSGraph()
graph.add_edges([(1,2,0),(1,4,0),(2,4,0),(2,3,0),(4,5,0),(5,2,0),(5,6,0),(6,3,0)])
graph2.set_vertex(4)
scc(graph)
scc(graph2)
