class GraphList:
    def __init__(self, vertices):
        self.vertices = vertices  # Initialize the list of vertices
        self.adjList = [[] for _ in range(vertices)]  # Create the empty list of vertices

    def addEdge(self, u, v):  # Simply adding the edge between u and v
        self.adjList[u].append(v)
        # self.adjList[v].append(u)

    def getGraph(self):
        return self.adjList

    def showList(self):
        # Print the list of vertices
        for vertex, neighbors in enumerate(self.adjList):
            print(f"V_{vertex}: {neighbors}")
