#
#   Genetic Algorithm for Shortest Path
#   Running the algorithm
#

from graph import Graph
from ShortestPathGA import ShortestPathGA

# testing create graph for now


def main():
    g = Graph(100)
    g.create_random_graph(0.90)
    sp = ShortestPathGA(g, 30)
    sp.simulate(plot=False, num_iter=400,
                num_couples=8, num_retain=3)
    print("GA path: ", sp.best_route, "\nCost: ", sp.min_dist)


if __name__ == "__main__":
    main()
