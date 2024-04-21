import time
import random
from generateGraph import generateRandomGraph
from dfsTopologicalSort import dfsTopologicalSort
from validInput import isValid, isNonZeroPositive, floatValid
from buildGraph import Graph
import matplotlib.pyplot as plt
import networkx as nx


def dfs(node, graph, visited, resultStack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, resultStack)
    resultStack.append(node)


def topologicalSort(graph):
    numberVertices = len(graph)
    visited = [False] * numberVertices
    resultStack = []

    start = time.time()

    for vertex in range(numberVertices):
        if not visited[vertex]:
            dfs(vertex, graph, visited, resultStack)

    end = time.time()
    timeTaken = (end - start) * 1000  # Convert to milliseconds

    return resultStack[::-1], timeTaken


for experiment in range(2000):
    vertices = random.randint(1, 100)
    density = random.uniform(0.1, 1.0)
    graph = generateRandomGraph(vertices, density)

    sortedGraph, timeTaken = topologicalSort(graph)
    print(f"For experiment #{experiment+1}: Vertices = {vertices}, and for Density = {density:.2f}, Time Taken: {timeTaken:.6f} milliseconds")

    with open('experiments.txt', 'a') as f:
        f.write(f"For experiment #{experiment+1}: Vertices = {vertices}, and for Density = {density:.2f}, Time Taken: {timeTaken:.6f} milliseconds\n")

    print("  ")
