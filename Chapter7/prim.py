#O((V+E)log(V))

from Dijkestra import PriorityQueue
from general_dfs import Graph

def prim(g, start):
    pq = PriorityQueue()
    start.distance = 0
    pq.heapify([(v.distance, v) for v in g])
    while pq:
        distance, current_v = pq.pop()
        for next_v in current_v.get_neighbors():
            new_distance = current_v.get_neighbor(next_v)
            if next_v in pq and new_distance < next_v.distance:
                next_v.previous = current_v
                next_v.distance = new_distance
                pq.change_priority(new_distance, next_v)
    
    weight = 0
    for vertex in g:
        weight += vertex.distance
    
    return weight 
