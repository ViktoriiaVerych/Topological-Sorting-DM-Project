import time
from generateGraph import generateRandomGraph
from dfsTopologicalSort import dfsTopologicalSort
from validInput import isValid, isNonZeroPositive, floatValid
from buildGraph import Graph


def main():
    while True:
        # Number of vertices from user's input
        vertices = int(isValid("Enter the number of vertices: ",
                               isNonZeroPositive,
                               "Invalid input. The number of vertices must be a positive integer."))

        # Density from user's input
        density = float(isValid("Enter the density (0-1): ",
                                floatValid,
                                "Invalid input. Density must be a number between 0 and 1."))

        print("  ")
        graphRepresent = input("Choose graph representation: \n"
                               "   - For matrix, enter \"Matrix\".\n"
                               "   - For list, enter \"List\".\n").capitalize()
        print("  ")

        # Ask the user what graph representation to show
        while graphRepresent not in ('Matrix', 'List', 'M', 'L'):
            print("Invalid input. Enter Matrix or List.")
            graphRepresent = input("Choose graph representation: \n"
                                   "- For matrix, enter \"Matrix\".\n"
                                   "- For list, enter \"List\".\n").capitalize()

        # Generate the graph using Erdős–Rényi model
        graph = generateRandomGraph(vertices, density)

        # Show the graph in matrix representation
        if graphRepresent == "Matrix" or graphRepresent == "M":
            graphLM = Graph(vertices)
            for u in range(vertices):
                for v in graph[u]:
                    graphLM.addEdge(u, v)
            graphLM.showMatrix()

        # Ask the user if they want to switch the representation to list
        switchRepresent = input("Do you want to generate the graph in list representation? \n").capitalize()
        if switchRepresent == "Yes" or switchRepresent == "Y":
            graphLM = Graph(vertices)
            for u in range(vertices):
                for v in graph[u]:
                    graphLM.addEdge(u, v)
            graphLM.showList()

        # Show the graph in list representation
        elif graphRepresent == "List" or graphRepresent == "L":
            graphLM = Graph(vertices)
            for u in range(vertices):
                for v in graph[u]:
                    graphLM.addEdge(u, v)
            graphLM.showList()

            # Ask the user if they want to switch the representation to matrix
            switchRepresent = input("Do you want to generate the graph in matrix representation? \n").capitalize()
            if switchRepresent == "Yes" or switchRepresent == "Y":
                graphLM = Graph(vertices)
                for u in range(vertices):
                    for v in graph[u]:
                        graphLM.addEdge(u, v)
                graphLM.showMatrix()

        print("  ")

        # Count the total amount of vertices & edges in the graph. Print it out
        edges_total = sum(len(adjList) for adjList in graph)
        print(f"G = <{{Vertices: {vertices} Edges: {edges_total}}}>")

        # Measure execution time
        start = time.time()

        # Do the topological sort
        sorted_order = dfsTopologicalSort(graph)
        end = time.time()

        # Show the topological sort, execution time
        print("Proposed topological sorting:", sorted_order)
        print("  ")
        print("Start:", start)
        print("End:", end)
        print("Execution time:", end - start, "sec")
        print("  ")

        # Ask the user if they want to repeat
        repeat = input("Do you want to repeat?: \n").upper()
        if repeat != "YES" and repeat != "Y":
            break


if __name__ == "__main__":
    main()
