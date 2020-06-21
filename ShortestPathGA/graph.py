#
#   Genetic Algorithm for Shortest Path
#   Create a graph to simulate the algorithm on
#

import random
import seaborn as sns
import matplotlib.pyplot as plt

# will be using adjacency matrix to represent the graph
# edge weights between 0 and 100 (exclusive) using a random distribution


class Graph(object):
    ''' Class to create a graph
    '''

    def __init__(self, num_nodes):
        ''' num_nodes: number of nodes in the graph
        '''
        self.num_nodes = num_nodes
        self.adj = None

    def create_random_graph(self, zero_prob=0.15):
        ''' Generating a random undirected weighted graph
        '''
        self.adj = [[0 for _ in range(self.num_nodes)]
                    for _ in range(self.num_nodes)]

        for row in range(0, self.num_nodes):
            for col in range(0, row):
                if random.random() > zero_prob:
                    self.adj[row][col] = random.random()
                self.adj[col][row] = self.adj[row][col]

    def display_graph(self):
        sns.heatmap(self.adj)
        plt.show()
