import random


# Erdős–Rényi model for generating random directed graphs
def generateRandomGraph(vertices, density):
    graph = [[] for _ in range(vertices)]
    for u in range(vertices):
        for v in range(vertices):
            if u != v and random.random() < density:
                graph[u].append(v)
    return graph

