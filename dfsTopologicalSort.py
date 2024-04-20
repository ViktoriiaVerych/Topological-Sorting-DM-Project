def dfsTopologicalSort(graph):
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        result_stack.append(node)

    numberVertices = len(graph)
    visited = [False] * numberVertices
    result_stack = []

    for vertex in range(numberVertices):
        if not visited[vertex]:
            dfs(vertex)

    return result_stack[::-1]


