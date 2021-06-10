import matplotlib.pyplot as plt
import networkx as nx

NOT_VISITED = (.5, .5, .5)
CURRENT = (1, 0, 0)
WAITING = (.5, 0, .5)
VISITED = (.5, .5, 1)


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


def render_graph(g: nx.Graph, position=None, labels=None, colors=None, save=True) -> None:
	# default values should not be mutable so :

	position = position or nx.spring_layout(g)
	labels = labels or {n: n for n in g.nodes}
	colors = colors or [NOT_VISITED for n in g.nodes]

	plt.clf()
	#plt.axis("off")

	# draw nodes

	nx.draw_networkx_nodes(g, position, node_size=700, node_color=colors)

	# draw edges

	nx.draw_networkx_edges(G, pos)

	# draw node labels

	nx.draw_networkx_labels(g, position, labels, font_size=8, font_family="sans-serif", font_color="white")

	# draw edge weights
	edge_labels = nx.get_edge_attributes(G, 'weight')
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_family="sans-serif", font_size=8)


	if not save:
		plt.show()
	else:
		plt.savefig('fig.svg')


G = nx.Graph()

G.add_weighted_edges_from(
	[('A', 'B', 20), ('A', 'C', 6), ('B', 'D', 2), ('C', 'D', 17), ('D', 'E', 10), ('D', 'F', 15), ('E', 'F', 6),
	 ('E', 'G', 2), ('F', 'G', 6)])

# pos = nx.spring_layout(G)  # positions for all nodes


pos = {'A': (0, 0), 'B': (2, 1), 'C': (2, -1), 'D': (4, 0), 'E': (6, 1), 'F': (6, -1), 'G': (8, 0)}
labels = {n: n + ' : \u221e' for n in G.nodes}

render_graph(G, position=pos, labels=labels)

print(dijkstra(G, 'A', 'G'))
