import time
import random
from generateGraph import generateRandomGraph
from dfsTopologicalSort import dfsTopologicalSort


def main():
    for _ in range(2000):
        # Random number of vertices
        vertices = random.randint(1, 100)

        # Random density
        density = random.random()

        graph = generateRandomGraph(vertices, density)

        # Measure execution time
        start = time.time()
        sorted_order = dfsTopologicalSort(graph)
        end = time.time()

        sortedGraph, timeTaken = dfsTopologicalSort(graph)
        print(
            f"For experiment #{_ + 1}: Vertices = {vertices}, and for Density = {density:.2f}, Time Taken: {timeTaken:.6f} milliseconds")

        # Write down all experiments to  experiments.txt
        with open('experiments.txt', 'a') as f:
            f.write(
                f"For experiment #{_ + 1}: Vertices = {vertices}, and for Density = {density:.2f}, Time Taken: {timeTaken:.6f} milliseconds\n")

        print("  ")


if __name__ == "__main__":
    main()
