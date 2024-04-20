def topologicalSort(graph):
    def removeEdge(u, v):
        graph[u].remove(v)

    num_vertices = len(graph)
    in_degree = [0] * num_vertices
    for u in range(num_vertices):
        for v in graph[u]:
            in_degree[v] += 1

    L = []
    S = [v for v in range(num_vertices) if in_degree[v] == 0]

    while S:
        n = S.pop()
        L.append(n)
        for m in graph[n]:
            removeEdge(n, m)
            if in_degree[m] == 0:
                S.append(m)

    if any(graph):
        print("Error occurred. Graph has at least one cycle.))))")
    else:
        print("Topologically sorted order):", L)
