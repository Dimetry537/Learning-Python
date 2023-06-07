import random
import networkx as nx
import planarity

def generate_planar_graph(n, m, i=0, max_iter=100):
    vertices = list(range(1, n+1))
    edges = []
    while len(edges) < m and i < max_iter:
        u, v = random.sample(vertices, 2)
        if (u, v) not in edges and (v, u) not in edges:
            edges.append((u, v))
        i += 1
    if not is_planar(vertices, edges):
        if i < max_iter:
            yield from generate_planar_graph(n, m, i)
    else:
        yield vertices, edges

def is_planar(vertices, edges):
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    return planarity.is_planar(G)

for vertices, edges in generate_planar_graph(3, 7):
    print("Vertices:", vertices)
    print("Edges:", edges)
