from general_dfs import DFSGraph

def topological_sort(graph):
    graph.dfs()
    vertices = list(graph)
    vertices.sort(key=lambda vertex: vertex.closing_time, reverse = True)
    return vertices
