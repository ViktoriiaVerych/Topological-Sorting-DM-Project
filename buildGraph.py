class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = [[] for _ in range(vertices)]
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def addEdge(self, u, v):

        # Add the edge to list
        self.adjList[u].append(v)
        self.adjList[v].append(u)

        # Add the edge to list
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def getAdjacencyList(self):
        return self.adjList

    def getAdjacencyMatrix(self):
        return self.matrix

    def showList(self):

        # Show the adjacency list
        for vertex, neighbors in enumerate(self.adjList):
            print(f"V_{vertex}: {neighbors}")

    def showMatrix(self):

        # Show the adjacency matrix
        print("   ", end="")
        for vertex in range(self.vertices):
            print(f"{vertex:2}", end=" ")
        print()

        for vertex, row in enumerate(self.matrix):
            print(f"{vertex:2} ", end="")
            for value in row:
                print(f"{value:2}", end=" ")
            print()

