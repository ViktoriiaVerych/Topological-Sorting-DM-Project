class GraphMatrix:
    def __init__(self, vertices):
        # Number of vertices in the graph initialized
        self.vertices = vertices
        # Matrix filled with zeros
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def addEdge(self, u, v):
        # Simply adding the edge between u and v
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def getGraph(self):
        return self.matrix

    def showMatrix(self):
        # Print the matrix
        print("   ", end="")
        for vertex in range(self.vertices):
            print(f"{vertex:2}", end=" ")
        print()

        for vertex, row in enumerate(self.matrix):
            print(f"{vertex:2} ", end="")
            for value in row:
                print(f"{value:2}", end=" ")
            print()
