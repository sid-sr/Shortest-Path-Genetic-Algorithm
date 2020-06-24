#
#   Genetic Algorithm for Shortest Path
#

import random
import matplotlib.pyplot as plt


class ShortestPathGA(object):

    def __init__(self, graph, pop_size):
        self.graph = graph
        self.pop_size = pop_size
        self.population = []
        self.scores = []
        self.min_dist = 10 ** 5
        self.best_route = []

    def create_path(self):
        path = [0]
        while True:
            gen = [i for i in range(self.graph.num_nodes) if (
                self.graph.adj[path[-1]][i] != 0)]
            next_node = random.choice(gen)
            path.append(next_node)
            if next_node == self.graph.num_nodes - 1:
                break
        return path

    def init_population(self):
        for _ in range(self.pop_size):
            self.population.append(self.create_path())

    def crossover(self, route_1, route_2):
        ''' Return 2 new routes after the crossover operation
        '''
        common = set(route_1).intersection(set(route_2))
        common.remove(0)
        common.remove(self.graph.num_nodes-1)

        if len(common):
            el = common.pop()
            cut_1 = route_1.index(el)
            cut_2 = route_2.index(el)
            new_r1 = route_1[:cut_1] + route_2[cut_2:]
            new_r2 = route_2[:cut_2] + route_1[cut_1:]
            return new_r1, new_r2
        else:
            return route_1, route_2

    def mutate(self, route, prob):
        ''' Swap nodes in the given routes with the given probability
        '''
        new_route = route[:]
        for i in range(1, len(new_route)-1):
            if random.random() < prob:
                options = [j for j in range(self.graph.num_nodes) if (
                    self.graph.adj[new_route[i-1]][j] != 0) and j != i]
                for node in options:
                    pos = -1
                    for j in range(1, len(new_route)-1):
                        if new_route[j] == node:
                            pos = j
                            break

                    check_1 = self.graph.adj[new_route[i]][new_route[pos+1]]
                    check_2 = self.graph.adj[new_route[pos]][new_route[i+1]]
                    check_3 = self.graph.adj[new_route[pos-1]][new_route[i]]

                    if pos != -1 and check_1 and check_2 and check_3:
                        new_route[pos], new_route[i] = new_route[i], new_route[pos]
                        break
        return new_route

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

    def simulate(self, plot=False, num_iter=1000, num_couples=3, num_retain=2):
        ''' Run the Genetic algorithm to find the shortest path
            between nodes 0 and N-1.
        '''
        self.init_population()
        dists = []

        for i in range(num_iter):
            new_pop = []
            self.set_scores()
            best_score = min(self.scores)
            best_ind = self.scores.index(best_score)
            best_path = self.population[best_ind]

            if self.min_dist > best_score:
                self.min_dist = best_score
                self.best_route = best_path

            dists.append(best_score)
            for _ in range(num_couples):
                old_r1 = self.population[self.select()]
                old_r2 = self.population[self.select()]
                r1, r2 = self.crossover(old_r1, old_r2)
                new_pop.extend([r1, r2])

            for j in range(len(new_pop)):
                new_pop[j] = self.mutate(new_pop[j], 0.15)

            new_pop.append(best_path)
            for j in range(num_retain):
                new_pop.append(self.population[self.select()])

            while self.pop_size - len(new_pop) > 0:
                new_pop.append(self.create_path())
            self.population = new_pop

        if plot:
            plt.plot(dists)
            plt.show()
