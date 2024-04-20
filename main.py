from buildGraph import generateRandomGraph
from dfsTopologicalSort import dfsTopologicalSort
from topologicalSort import topological_sort

def isValid(s):
    return s.strip() and not any(char.isdigit() or char in {'-', '+', '.', ' '} for char in s)

def main():
    while True:
        vertices = input("Enter the number of vertices: ")
        while not vertices.isdigit() or int(vertices) <= 0:
            print("Invalid input. The number of vertices must be a positive integer.")
            vertices = input("Enter the number of vertices: ")

        density = input("Enter the density (0-1): ")
        while not all(char.isdigit() or char == '.' for char in density) or float(density) <= 0 or float(density) > 1:
            print("Invalid input. Density must be a number between 0 and 1.")
            density = input("Enter the density (0-1): ")

        vertices = int(vertices)
        density = float(density)

        graph = generateRandomGraph(vertices, density)
        print("--------------------------------\n")
        print("Generated graph:", graph)

        algorithm = input(
            "--------------------------------\n"
            "Choose the type of sorting:\n - For topological sort, enter \"TS\".\n - For DFS topological sort, enter \"DS\": ").upper()
        while not isValid(algorithm) or algorithm not in {"TS", "DS"}:
            print("Invalid input. Choose topological sort (TS) or DFS topological sort (DS).")
            algorithm = input(
                "Choose the type of sorting:\n - For topological sort, enter \"TS\".\n - For DFS topological sort, enter \"DS\": ").upper()

        if algorithm == "TS":
            sortedOrder = topological_sort(graph)
        elif algorithm == "DS":
            sortedOrder = dfsTopologicalSort(graph)

        print("Proposed topological sorting:", sortedOrder)

        repeat = input("Do you want to repeat? : ").upper()
        if repeat != "YES" and repeat != "Y":
            break


if __name__ == "__main__":
    main()
