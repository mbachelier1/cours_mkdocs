import matplotlib.pyplot as plt
import networkx as nx



def dijkstra(graph: nx.Graph, start, end):
    nodes = list(graph.nodes)
    d = {node: float('inf') for node in nodes}
    d[start] = 0
    pred = dict()
    while nodes:
        print(f"Remaining nodes  and distances: {d}.")
        a = min((n for n in d if n in nodes), key=lambda x: d[x])
        nodes.remove(a)
        print(f"closest : {a}")
        for b in graph.neighbors(a):
            if b in nodes and d[b] > d[a] + graph.edges[(a, b)]['weight']:
                d[b] = d[a] + graph.edges[(a, b)]['weight']
                pred[b] = a

    result = [end]
    while pred[result[0]] != start:
        result = [pred[result[0]]] + result
    return [start] + result, d

plt.clf()
G = nx.Graph()

G.add_weighted_edges_from([('A', 'B', 20), ('A', 'C', 6), ('B', 'D', 2), ('C', 'D', 17), ('D', 'E', 10), ('D', 'F', 15),
                           ('E', 'F', 6), ('E', 'G', 2),
                           ('F', 'G', 6)])

#pos = nx.spring_layout(G)  # positions for all nodes


pos = {'A':(0,0),'B':(2,1),'C':(2,-1),'D':(4,0),'E':(6,1),'F':(6,-1),'G':(8,0)}
labels = {n:n+' : \u221e' for n in G.nodes}
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos)

# labels
nx.draw_networkx_labels(G, pos, labels,font_size=8, font_family="sans-serif", font_color="white")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_family="sans-serif", font_size=8)
plt.axis("off")
plt.tight_layout()
plt.savefig("hey.svg")
L = nx.algorithms.shortest_paths.weighted.dijkstra_path(G, 'A', 'G')
print(L)
print(dijkstra(G, 'A', 'G'))
