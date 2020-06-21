#
#   Genetic Algorithm for Shortest Path
#   Running the algorithm
#

from graph import Graph
from ShortestPathGA import ShortestPathGA

# testing create graph for now


def main():
    g = Graph(100)
    g.create_random_graph(0.9)
    sp = ShortestPathGA(g, 20)
    sp.simulate(plot=True, num_iter=40,
                num_couples=8, num_retain=3)
    print(sp.best_route)
    print(sp.min_dist)

if __name__ == "__main__":
    main()
