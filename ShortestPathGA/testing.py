#
#   Genetic Algorithm for Shortest Path
#   Running the algorithm
#

from graph import Graph
from ShortestPathGA import ShortestPathGA

# testing create graph for now


def main():
    g = Graph(100)
    g.create_random_graph(0.8)
    sp = ShortestPathGA(g, 10)
    sp.init_population()
    sp.set_scores()
    print(sp.select())

if __name__ == "__main__":
    main()
