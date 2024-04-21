def dfsTopologicalSort(graph):
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        resultStack.append(node)
    # Variables initialized
    numberVertices = len(graph)
    visited = [False] * numberVertices
    resultStack = []
    # Do DFS travers for each unvisited vertex
    for vertex in range(numberVertices):
        if not visited[vertex]:
            dfs(vertex)
    # Return the sorted reversed order
    return resultStack[::-1]
