import heapq
from task_1 import *


def dijkstra(graph, start):
    shortest_paths = {vertex: float("infinity") for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight["weight"]
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return shortest_paths


print(dijkstra(G, "Я"))
