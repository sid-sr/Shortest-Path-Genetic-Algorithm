#
#   Genetic Algorithm for Shortest Path
#   Create a graph to simulate the algorithm on
#

import numpy as np
import random

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

    def create_random_graph(self, zero_prob=0.15, max_dist=100):
        ''' Generating a random undirected weighted graph
        '''
        self.adj = np.random.rand(self.num_nodes, self.num_nodes)
        self.adj[self.adj < zero_prob] = 0
        non_zero_pos = self.adj[self.adj >= zero_prob].shape[0]
        self.adj[self.adj >= zero_prob] = np.random.randint(
            1, max_dist+1, size=non_zero_pos)
