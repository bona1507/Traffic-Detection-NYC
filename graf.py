import networkx as nx
import matplotlib.pyplot as plt

# Import object modules
import cam1

# Get weight values from each object
weights = {
    "Cam 1": cam1.get_weight(),
    "Object 2": 10
}

# Find the object with the heaviest weight
heaviest_object = max(weights, key=weights.get)

# Create an empty weighted graph
G = nx.Graph()

# Add nodes with labels
for label, weight in weights.items():
    G.add_node(label, weight=weight)

# Create edges between nodes (e.g., connecting all pairs of nodes)
for i, (label_i, weight_i) in enumerate(weights.items()):
    for label_j, weight_j in list(weights.items())[i + 1:]:
        G.add_edge(label_i, label_j, weight=abs(weight_i - weight_j))

# Get node weights
node_weights = nx.get_node_attributes(G, "weight")

# Create a weighted graph layout
pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1000)

# Draw edges with weights
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
nx.draw_networkx_edges(G, pos, alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, labels=node_weights, font_size=12)

# Show the weighted graph
plt.title(f"Weighted Graph - Heaviest Object: {heaviest_object}")
plt.axis("off")
plt.show()
