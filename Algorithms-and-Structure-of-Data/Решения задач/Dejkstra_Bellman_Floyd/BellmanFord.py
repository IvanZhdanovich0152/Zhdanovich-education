import networkx as nx
import matplotlib.pyplot as plt

EDGES = [
    ('S', 'A', 7),
    ('S', 'C', 6),
    ('S', 'F', 5),
    ('S', 'E', 6),
    ('A', 'B', 4),
    ('A', 'C', -2),
    ('B', 'G', -2),
    ('B', 'H', -4),
    ('C', 'D', 2),
    ('C', 'F', 1),
    ('F', 'D', 3),
    ('E', 'F', -2),
    ('E', 'H', 3),
    ('H', 'G', 1),
    ('G', 'I', -1),
    ('I', 'H', 1),
]
START = 'S'

def bellman_ford(edges, start):
    vertices = {start}
    for u, v, _ in edges:
        vertices.add(u)
        vertices.add(v)

    dist = {v: float('inf') for v in vertices}
    prev = {v: None for v in vertices}
    dist[start] = 0

    iterations = []

    for i in range(len(vertices) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        iterations.append(dict(dist))

        if not updated:
            break

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("The graph contains a negative cycle!")

    return dist, prev, iterations


def visualize_tree(edges, prev, dist, start):
    G = nx.DiGraph()
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)

    pos = {
        'S': (0, 0),
        'A': (-2, 2),
        'B': (-3, 0),
        'C': (0, 2),
        'D': (2, 2),
        'F': (2, 0),
        'E': (2, -2),
        'G': (-2, -2),
        'H': (0, -2),
        'I': (-3, -3),
    }

    tree_edges = []
    for v, u in prev.items():
        if u is not None:
            tree_edges.append((u, v))

    plt.figure(figsize=(10, 7))

    nx.draw_networkx_edges(G, pos, edge_color='lightgray',
                           width=1.5, arrows=True, arrowsize=18)

    nx.draw_networkx_edges(G, pos, edgelist=tree_edges,
                           edge_color='red', width=3,
                           arrows=True, arrowsize=25)

    nx.draw_networkx_nodes(G, pos, node_color='lightyellow',
                           node_size=1000, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=14)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels,
                                 font_size=10)

    for n, (x, y) in pos.items():
        d = dist[n]
        plt.text(x, y - 0.25, 'inf' if d == float('inf') else str(d),
                 ha='center', fontsize=11, color='blue')

    plt.title(f"Bellman-Ford: shortest path tree from {start}")
    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    dist, prev, iterations = bellman_ford(EDGES, START)
    print(iterations)

    print("Final distance: ")
    for v in sorted(dist):
        d = dist[v]
        print(f"  {v}: {'inf' if d == float('inf') else d}")

    print("\nshortest path tree (edge -> prev vertex):")
    for v in sorted(prev):
        if prev[v] is not None:
            print(f"  {prev[v]} -> {v}")

    visualize_tree(EDGES, prev, dist, START)