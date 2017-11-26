import unittest
import random
import networkx as nx
import src.BellmanFord as BellmanFord

def construct_nx_graph(g):
    '''
    * Constructs the directed graph using the NetworkX library
    * Adds all nodes, edges, and weights from input dict
    :param g: input dictionary representing graph
    :return dg: Directed graph using networkx library
    '''
    dg = nx.DiGraph()

    for node in g:
        dg.add_node(node)

    for node in g:
        for edge, weight in g[node]:
            dg.add_edge(node, edge, weight=weight)

    return dg

def random_graphs():
    '''
    * Constructs set directed graph with random weights
    :return: dict representing graph and a NetworkX version
    '''
    g = {0: [(1, rand_weight())],
         1: [(2, rand_weight()), (3, rand_weight())],
         2: [(3, rand_weight())],
         3: [(4, rand_weight()), (5, rand_weight()), (6, rand_weight())],
         4: [],
         5: [(6, rand_weight())],
         6: []
    }

    return (g, construct_nx_graph(g))

def rand_weight(start=1, end=20):
    '''
    * Returns random weight for graph
    '''
    return random.randint(start, end)

class TestAlg(unittest.TestCase):
    def test_dist_to_target(self):
        '''
        * Generates set directed graph with random weights
        * Checks correctness of algorithm to library's for 
          shortest distance to target node
        '''
        g, nx_g = random_graphs()

        nx_dist = nx.bellman_ford_path_length(nx_g, 0, 6)
        my_dist = BellmanFord.bellman_ford(g, 0, target=6)

        self.assertEqual(nx_dist, my_dist)

    def test_dist_to_all(self):
        '''
        * Generates set directed graph with random weights
        * Checks correctness of algorithm to library's for 
          shortest distance to all nodes
        '''
        g, nx_g = random_graphs()

        nx_dists = nx.single_source_bellman_ford_path_length(nx_g, 0)
        my_dists = BellmanFord.bellman_ford(g, 0)

        check = True

        for node in g:
            if nx_dists[node] != my_dists[node]:
                check = False

        self.assertTrue(check)
    
    def test_path_to_target(self):
        '''
        * Generates set directed graph with random weights
        * Checks correctness of algorithm to library's for 
          shortest path to target node
        '''
        g, nx_g = random_graphs()

        my_path = BellmanFord.bf_paths(g, 0, target=6)
        nx_path = nx.bellman_ford_path(nx_g, 0, 6)

        self.assertEqual(my_path, nx_path)

    def test_path_to_all(self):
        '''
        * Generates set directed graph with random weights
        * Checks correctness of algorithm to library's for 
          shortest path to all nodes
        '''
        g, nx_g = random_graphs()

        nx_paths = nx.single_source_bellman_ford_path(nx_g, 0)
        my_paths = BellmanFord.bf_paths(g, 0)

        check = True
        for node in g:
            if nx_paths[node] != my_paths[node]:
                check = False

        self.assertTrue(check)


    def test_neg_cycle(self):
        '''
        * Tests that Bellman Ford algorithm correctly finds
          the negative cycle
        '''
        g = {0: [(1, 2)],
             1: [(2, 8), (3, 5)],
             2: [(3, -5)],
             3: [(4, 4), (5, -2), (6, 1)],
             4: [(3, -5)],
             5: [(6, 6)],
             6: []
        }
        self.assertIsNone(BellmanFord.bellman_ford(g, 0))

    def test_neg_cycle_2(self):
        '''
        * Tests that Bellman Ford algorithm correctly finds
          the negative cycle
        '''
        g = {0: [(1, 2)],
             1: [(2, 8), (3, 5)],
             2: [(3, -5)],
             3: [(2, 2)]
        }
        self.assertIsNone(BellmanFord.bellman_ford(g, 0))



if __name__ == '__main__':
    unittest.main()