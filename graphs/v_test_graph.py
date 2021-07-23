from graph import *
import networkx as nx
import matplotlib.pyplot as plt

g = Graph()

# adding some vertices
for i in range(5):
    g.add_vertex(i)

print(g.vertices)

# adding some edges
g.add_edge(0,1,4)
g.add_edge(0,2,3)
g.add_edge(0,3,6)
g.add_edge(0,4,5)
g.add_edge(1,2,7)
g.add_edge(1,3,1)
g.add_edge(2,3,8)
g.add_edge(2,4,6)

# print the str representation of each vertex
for v in g:
    print(str(v))

# print edges with the format (V_origin, V_destination)[weight]
for v in g:
    for w in v.get_connections():
        print(f"({v.get_id()} -> {w.get_id()})[{v.get_weight(w)}]")

# From https://www.geeksforgeeks.org/visualize-graphs-in-python/
class GraphVisualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

G = GraphVisualization()

for v in g:
    for w in v.get_connections():
        G.addEdge(v.get_id(), w.get_id())

G.visualize()
