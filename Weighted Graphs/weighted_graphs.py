class WeightedDigraph:
    def __init__(self):
        self.g = {}

    def add_node(self, node):
        if node in self.g:
            raise ValueError("Node already in Graph")
        self.g[node] = []

    def add_edge(self, src, dest, weight):
        if src not in self.g:
            return ValueError("Source isn't in Graph")
        if dest not in self.g:
            return ValueError("Destination isn't in Graph")

        nexts = self.g[src]
        if dest in nexts:
            return
        nexts.append((dest, weight))


g = WeightedDigraph()
nodes = ['a', 'b', 'c', 'd', 'e']
for n in nodes:
    g.add_node(n)

edges = [
    ('a', 'b', 4),
    ('a', 'c', 1),
    ('b', 'd', 8),
    ('c', 'e', 25),
    ('e', 'd', 3)
]
for e in edges:
    g.add_edge(e[0], e[1], e[2])

import pprint
print("Printing The WEIGHTED DiGraph")
pprint.pprint(g.g)


def traverse_graph(self, start):
    q = [start]
    visited = []

    while q:
        current = q.pop(0)

        # if we've already visited it, we can skip
        if current in visited:
            continue
        print(current)

        # We're done with the current
        visited.append(current)

        # Get all directly connected nodes
        next_nodes = self.g[current]

        # Traverse all the nexts
        for n in next_nodes:
            q.append(n[0])  # get node only instead of (dest, weight)


WeightedDigraph.traverse_graph = traverse_graph
print("\n WEIGHTED DIGRAPH TRAVERSAL")
g.traverse_graph('a')


def find_shortest_dijkstra(self, src):
    # Mark all nodes unvisited and store them
    to_visit = list(self.g.keys())

    print("To visit: " + str(to_visit))

    # Set the distance to zero for our initial node and to infinity for other nodes.
    inf = float('inf')  # That's python for infinity
    dists = {node: inf for node in to_visit}
    dists[src] = 0
    print("All Distances" + str(dists))

    # Let's loop
    while to_visit:
        print("--------")

        # Select the unvisited node with smallest distance
        # can't compare 'a' with 'b'. So, we compare dist['a'] with dist['b']
        current = min(to_visit, key=lambda node: dists[node])
        print("Current:" + current)

        # Check to make sure min distance isn't infinity
        if dists[current] == inf:
            break
        # Find unvisited neighbours for the current node
        nexts = self.g[current]
        unvisited_neighbours = []
        for n in nexts:
            if n[0] in to_visit: # recall that n is e.g. ('b', 5)
                unvisited_neighbours.append(n)
        print("Unvisited Neighbours of " + current + ":" + str(unvisited_neighbours))

        # Calculate their distances through the current node
        for n in unvisited_neighbours:
            label = n[0]
            dist_to = n[1]

            old_distance = dists[label]
            new_distance = dists[current] + dist_to

            # See which is better: old best distance or this one
            if new_distance < old_distance:
                dists[label] = new_distance

        print("All Distances " + str(dists))
        # current is now visited
        to_visit.remove(current)

        # break         # break after each iteration for demo


WeightedDigraph.find_shortest_dijkstra = find_shortest_dijkstra

print("\n Shortest Path via Dijkstra")
g.find_shortest_dijkstra('a')