import networkx as nx
import matplotlib.pyplot as plt



graph = {
    "Прадід": {"Дід": {"weight": 5}},
    "Дід": {"Бабуся": {"weight": 4}, "Мама": {"weight": 3}, "Дядько": {"weight": 3}},
    "Бабуся": {"Мама": {"weight": 3}, "Дядько": {"weight": 3}},
    "Мама": {"Батько": {"weight": 2}, "Я": {"weight": 1}},
    "Дядько": {"Брат": {"weight": 3}},
    "Батько": {"Я": {"weight": 1}},
    "Я": {"Брат": {"weight": 3}}
}

G = nx.Graph(nx.from_dict_of_dicts(graph))


pos = nx.spring_layout(G)
nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [{node: deg} for node, deg in G.degree()]


if __name__ == "__main__":
    print(f"Кількість вершин: {num_nodes} дорівнює кількості родичів")
    print(f"Кількість ребер: {num_edges} дорівнює кількості зв'язків між родичами")
    print(f"Ступені вершин {degrees} дорівнює кількості зв'язків кожного з родичів")
 

    plt.show()



if __name__ == "task_3.py":
    graph