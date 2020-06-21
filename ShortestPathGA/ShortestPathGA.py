#
#   Genetic Algorithm for Shortest Path
#

# Work in progress -> skeletons defined

from graph import Graph
import random

class ShortestPathGA(object):

    def __init__(self, graph, pop_size):
        self.graph = graph
        self.pop_size = pop_size
        self.population = []
        self.scores = []

    def create_path(self):
        path = [0]
        while True:
            gen = [i for i in range(self.graph.num_nodes) if (self.graph.adj[path[-1]][i] != 0)] 
            next_node = random.choice(gen)
            path.append(next_node)
            if next_node == self.graph.num_nodes - 1:
                break
        return path        

    def init_population(self, size=10):
        for _ in range(size):
            self.population.append(self.create_path())

    def crossover(self):
        pass

    def mutate(self):
        pass

    def fitness(self, path):
        ''' Return the cost for the given path
        '''
        cost = 0.0
        for node_num in range(1, len(path)):
            cost += self.graph.adj[path[node_num]][path[node_num-1]]
        return cost

    def set_scores(self):
        ''' Set the score of each path in a population 
        '''
        self.scores = [self.fitness(path) for path in self.population]

    def select(self):
        ''' Return an index of the path to select
        '''
        arr = sorted([[self.scores[i], i] for i in range(self.pop_size)])
        ordering = [0 for _ in range(self.pop_size)]
        for ind, pair in enumerate(arr, 0):
            ordering[pair[1]] = self.pop_size - ind
        
        prefix = [ordering[0]]
        for i in range(1, self.pop_size):
            prefix.append(prefix[-1] + ordering[i])
        prob_dist = [el/prefix[-1] for el in prefix]

        random_num = random.random()
        for index in range(self.pop_size):
            if prob_dist[index] >= random_num:
                return index

    def simulate(self):
        pass
