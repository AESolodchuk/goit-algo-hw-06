from task_1 import *
from collections import deque


def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []
    if start not in visited:
        visited.add(start)
        if parent is not None:
            path.append((parent, start))
        for next in graph[start]:
            dfs(graph, next, visited, path, start)
    return path


def bfs(graph, start):
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    return path



dfs_path = dfs(G, "Прадід")
bfs_path = bfs(G, "Прадід")


print(f"DFS шлях: {dfs_path}")
print(f"BFS шлях: {bfs_path}")
