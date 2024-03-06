from task_1 import *
import matplotlib.pyplot as plt
import networkx


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='Я')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Я')

#print(shortest_paths)  # виведе найкоротші шляхи від вузла 'A' до всіх інших вузлів
print(dijkstra(shortest_path_lengths,'Я'))  # виведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів
