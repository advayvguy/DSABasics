from GraphADT import Graph, Vertex

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