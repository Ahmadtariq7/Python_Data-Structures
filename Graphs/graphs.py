# import matplotlib
# import networkx as nx
# import matplotlib.pyplot as plt
# # %matplotlib inline
# import warnings
#
# warnings.filterwarnings("ignore")
#
#
# def draw_graph_with_nx(G):
#     pos = nx.spring_layout(G, iterations=200)
#     options = {'node_color': 'white', 'alpha': 1, 'node_size': 2000, 'width': 0.002, 'font_color': 'darkred',
#                'font_size': 25, 'arrows': True, 'edge_color': 'brown',
#                'arrowstyle': 'Fancy, head_length=1, head_width=1, tail_width=.4'}
#     labels = nx.get_node_attributes(G, 'label')
#     nx.draw(G, pos, labels=labels, **options)
#     plt.show()


class Digraph:
    def __init__(self):
        self.g = {}

    def addNode(self, node):
        if node in self.g:
            raise ValueError("Noe already in graph")

        self.g[node] = []

    def addEdge(self, src, dst):
        # Sanity Checks
        if src not in self.g or dst not in self.g:
            return
        else:
            nexts = self.g[src]
            if dst in nexts:
                return
            nexts.append(dst)

    # def draw_graph(self):
    #     G = nx.Digraph()
    #     for src in self.g:
    #         G.add_node(src, label=src)
    #         for dest in self.g[src]:
    #             G.add_edge(src, dest)
    #
    #     draw_graph_with_nx(G)


g = Digraph()
nodes = ['a', 'b', 'c', 'd', 'e', 'f']
for n in nodes:
    g.addNode(n)

edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('b', 'd'),
    ('c', 'd'),
    ('d', 'c'),
    ('e', 'f'),
    ('f', 'c'),
]
for e in edges:
    g.addEdge(e[0], e[1])

# kinda Main
print("printing graph in simple way")
print(g.g)  # Abstraction Police: Don't Freak out! We are just Looking
import pprint  # Pretty Printing

print("\nPrinting Graph using PPRINT")
pprint.pprint(g.g)


# print("\nPrinting using networkx ")
# g.draw_graph()  Will Work on Jupyter Notebook....

def traverse_graph(self, start):
    q = [start]
    visited = []

    while q:
        current = q.pop(0)
        # IF WE've visited, we can skip
        if current in visited:
            continue
        print(current)
        # We are done with current
        visited.append(current)
        # Get all connected nodes
        next_nodes = self.g[current]
        # Traverse all the nexts
        for n in next_nodes:
            q.append(n)


Digraph.traverse_graph = traverse_graph

print("\nGraph Traversal")
g.traverse_graph('e')


def find_path(self, start, end, path=[]):
    """Find path (not shortest) from start to end"""
    # Sanity Check
    if start not in self.g or end not in self.g:
        return ValueError("Source/End node not in graph")
    # Save the path we have traversed till now
    path = path + [start]
    # Base Case
    if start == end:
        return path
    # Recursive Case
    for node in self.g[start]:
        # Need to avoid Cycles
        if node not in path:
            # Find path from next node to
            newpath = self.find_path(node, end, path)
            if newpath:
                return newpath
    # If no path can be found from any of next nodes to end, there is no path!!
    return None


Digraph.find_path = find_path

print("\nPATH FINDING")
print(g.find_path('a', 'd'))
print(g.find_path('b', 'f'))
print(g.find_path('b', 'd'))


def find_all_paths(self, start, end, path=[]):
    # Sanity Check
    if start not in self.g or end not in self.g:
        return ValueError("Source/End node not in graph")
    # Save the path we have traversed till now
    path = path + [start]
    # Base Case
    if start == end:
        return [path]  # return the path in list since we may have many

    all_paths = []

    # recursive Call
    for node in self.g[start]:
        # Need to avoid Cycles
        if node not in path:
            # Find path from next node to
            all_newpaths = self.find_all_paths(node, end, path)
            for newpath in all_newpaths:
                all_paths.append(newpath)

    return all_paths


Digraph.find_all_paths = find_all_paths

print("\nFIND ALL PATHS")
print(g.find_all_paths('a', 'd'))


def find_shortest_path(self, start, end, path=[]):
    """Find path (not shortest) from start to end"""
    # Sanity Check
    if start not in self.g or end not in self.g:
        return ValueError("Source/End node not in graph")
    # Save the path we have traversed till now
    path = path + [start]
    # Base Case
    if start == end:
        return path

    shortest = None
    # Recursive Case
    for node in self.g[start]:
        # Need to avoid Cycles
        if node not in path:
            # Find path from next node to
            newpath = self.find_path(node, end, path)
            if newpath:
                if shortest is None or len(newpath) < len(shortest):  # Change
                    shortest = newpath

    return shortest


Digraph.find_shortest_path = find_shortest_path

print("\nFIND SHORTEST PATHS")
print(g.find_shortest_path('a', 'd'))
