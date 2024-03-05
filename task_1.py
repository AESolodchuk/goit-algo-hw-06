import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


G.add_nodes_from(["Прадід","Дід","Бабуся","Мама","Батько","Дядько","Брат"])


G.add_edges_from([
    ("Прадід", "Дід", {'weight': 5}),
    ("Дід", "Бабуся", {'weight': 4}),
    ("Дід", "Мама", {'weight': 3}),
    ("Бабуся", "Мама", {'weight': 3}),
    ("Бабуся", "Дядько", {'weight': 3}),
    ("Дід", "Дядько", {'weight': 3}),
    ("Мама", "Батько", {'weight': 2}),
    ("Мама", "Я", {'weight': 1}),
    ("Батько", "Я", {'weight': 1}),
    ("Дядько", "Брат", {'weight': 3}),
    ("Брат", "Я", {'weight': 3})
])

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [{node: deg} for node, deg in G.degree()]


if __name__== "__main__":
    print(f"Кількість вершин: {num_nodes} дорівнює кількості родичів")
    print(f"Кількість ребер: {num_edges} дорівнює кількості зв'язків між родичами")
    print("Ступені вершин дорівнює кількості зв'язків кожного з родичів:")
    for item in degrees:
        for key, value in item.items():
            print(key, value)
    
    plt.show()