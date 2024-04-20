import random

def generateRandomGraph(vertices, density):
    graph = [[] for _ in range(vertices)]
    for u in range(vertices):
        for v in range(u + 1, vertices):
            if random.random() < density:
                graph[u].append(v)
    return graph
