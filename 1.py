import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Ada", "Sabina", "Lukas", "Vera", "Randelon", "Marta", "John", "Mark", "Gloria"])
G.add_edges_from([("Ada", "Sabina"), ("Ada", "Lukas"), ("Sabina", "Lukas"), ("Sabina", "Gloria"), ("Gloria", "Vera"), ("John", "Vera"), ("John", "Ada"), ("John", "Randelon"), ("John", "Mark"), ("John", "Marta"), ("Vera", "Randelon"), ("Marta", "Randelon"), ("Vera", "Sabina"), ("Mark", "Gloria"), ("Mark", "Ada")])

num_nodes = G.number_of_nodes()  # 9
num_edges = G.number_of_edges()  # 15

nx.draw(G, with_labels=True)
plt.show()

print(num_nodes)
print(num_edges)
