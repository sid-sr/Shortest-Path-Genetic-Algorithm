#
#   Genetic Algorithm for Shortest Path
#   Running the algorithm
#

from graph import Graph
from ShortestPathGA import ShortestPathGA
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# testing create graph for now


def main():
    g = Graph(100)
    g.create_random_graph(0.90)
    sp = ShortestPathGA(g, 30)
    sp.simulate(plot=False, num_iter=400,
                num_couples=8, num_retain=3)
    G = nx.from_numpy_matrix(np.matrix(g.adj))

    def func(u, v, edge):
        return g.adj[u][v]

    shortestPath = nx.dijkstra_path(
        G, source=0, target=99, weight=func)
    print("Optimal shortest path (by Dijsktra): ", shortestPath,
          "\nCost: ", sp.fitness(shortestPath))
    print("GA path: ", sp.best_route, "\nCost: ", sp.min_dist)


if __name__ == "__main__":
    main()
