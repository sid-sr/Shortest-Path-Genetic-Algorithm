#
#   Genetic Algorithm for Shortest Path
#   Running the algorithm
#

from graph import Graph

# testing create graph for now


def main():
    g = Graph(5)
    g.create_random_graph(zero_prob=0.5, max_dist=50)
    print(g.adj)


if __name__ == "__main__":
    main()
