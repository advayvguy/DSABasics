from GraphADT import Graph, Queue

#O(V + E)

def build_graph(filename):
    buckets = {}
    graph = Graph()
    with open(filename, "r", encoding='utf8') as file_in:
        all_words = file_in.readlines()

    for line in all_words:
        word = line.strip()

        for i in range(len(word)):
            bucket = f"{word[:i]}_{word[i+1:]}"
            if bucket not in buckets:
                buckets[bucket] = []
            buckets[bucket].append(word)
    
    for bucket, words in buckets.items():
        for word in words:
            for neighbor in words:
                if word != neighbor:
                   graph.add_edge(word, neighbor)

    return graph 

def bfs(start, target):
    vert_Queue = Queue()
    vert_Queue.enqueue(start)
    while vert_Queue.size() > 0:
        current = vert_Queue.dequeue()
        if current == target:
            return 
        for neighbor in current.get_neighbors():
            if neighbor.color == 'white':
                neighbor.color = 'grey'
                neighbor.distance = current.distance + 1
                neighbor.previous = current 
                vert_Queue.enqueue(neighbor)
        current.color = 'black'

def traverse(starting_vertex):
    current = starting_vertex
    while current:
        print(current.key, end="")
        if current.previous is not None:
            print(" -> ",end="")
        current = current.previous
    print("\n")


def driver(start, stop, filename):
    graph = build_graph(filename)
    start_vertex = graph.get_vertex(start)
    stop_vertex = graph.get_vertex(stop)
    bfs(stop_vertex, start_vertex)
    traverse(start_vertex)

driver("COLD","WARM","dictionary.txt")