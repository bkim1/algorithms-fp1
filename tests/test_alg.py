import unittest
import random
import networkx as nx
import src.BellmanFord as BF
import src.Dijkstra as Dijkstra

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

def rand_graphs():
    '''
    * Constructs set directed graph with random weights
    * Graph has 7 nodes with set edges but randomized weights

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

def rand_graphs_2():
    '''
    * Constructs set directed graph with random weights
    * Graph has 12 nodes with set edges but randomized weights

    :return: dict representing graph and a NetworkX version
    '''
    g = {0: [(1, rand_weight()), (8, rand_weight())],
         1: [(2, rand_weight())],
         2: [(3, rand_weight())],
         3: [(4, rand_weight()), (6, rand_weight())],
         4: [(5, rand_weight()), (7, rand_weight())],
         5: [(7, rand_weight())],
         6: [(8, rand_weight()), (9, rand_weight())],
         7: [(11, rand_weight())],
         8: [(10, rand_weight())],
         9: [(10, rand_weight()), (11, rand_weight())],
         10: [(11, rand_weight())],
         11: []
    }

    return (g, construct_nx_graph(g))

def rand_graphs_3():
    '''
    * Constructs set directed graph with random weights
    * Graph has 16 nodes with set edges but randomized weights

    :return: dict representing graph and a NetworkX version
    '''
    g = {0: [(1, rand_weight())],
         1: [(2, rand_weight()), (6, rand_weight())],
         2: [(3, rand_weight())],
         3: [(4, rand_weight()), (6, rand_weight())],
         4: [(5, rand_weight())],
         5: [(6, rand_weight()), (11, rand_weight())],
         6: [(7, rand_weight()), (8, rand_weight()), (10, rand_weight())],
         7: [(9, rand_weight())],
         8: [(9, rand_weight()), (12, rand_weight())],
         9: [(10, rand_weight()), (12, rand_weight()), (15, rand_weight())],
         10: [(11, rand_weight())],
         11: [(13, rand_weight())],
         12: [(13, rand_weight())],
         13: [(14, rand_weight())],
         14: [(15, rand_weight())],
         15: []
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
        g, nx_g = rand_graphs()

        nx_dist = nx.bellman_ford_path_length(nx_g, 0, 6)
        bf_dist = BF.bellman_ford(g, 0, target=6)
        dj_dist = Dijkstra.dij(g, 0, t=6)

        self.assertEqual(nx_dist, bf_dist)
        self.assertEqual(dj_dist, nx_dist)

    def test_dist_to_target_100(self):
        check = True

        for _ in range(33):
            g, nx_g = rand_graphs()
            nx_dist = nx.bellman_ford_path_length(nx_g, 0, 6)
            bf_dist = BF.bellman_ford(g, 0, target=6)
            dj_dist = Dijkstra.dij(g, 0, t=6)

            if nx_dist != bf_dist or nx_dist != dj_dist:
                check = False
                break

        for _ in range(33):
            g, nx_g = rand_graphs_2()
            nx_dist = nx.bellman_ford_path_length(nx_g, 0, 11)
            bf_dist = BF.bellman_ford(g, 0, target=11)
            dj_dist = Dijkstra.dij(g, 0, t=11)

            if nx_dist != bf_dist  or nx_dist != dj_dist:
                check = False
                break

        for _ in range(33):
            g, nx_g = rand_graphs_3()
            nx_dist = nx.bellman_ford_path_length(nx_g, 0, 11)
            bf_dist = BF.bellman_ford(g, 0, target=11)
            dj_dist = Dijkstra.dij(g, 0, t=11)

            if nx_dist != bf_dist  or nx_dist != dj_dist:
                check = False
                break

        self.assertTrue(check)

    def test_dist_to_all(self):
        '''
        * Generates set directed graph with random weights
        * Checks correctness of algorithm to library's for 
          shortest distance to all nodes
        '''
        g, nx_g = rand_graphs()

        nx_dists = nx.single_source_bellman_ford_path_length(nx_g, 0)
        bf_dists = BF.bellman_ford(g, 0)
        dj_dists = Dijkstra.dij(g, 0)

        # print(dj_dists)

        check = True

        for node in g:
            if nx_dists[node] != bf_dists[node] or nx_dists[node] != dj_dists[node]:
                check = False

        self.assertTrue(check)
    
    def test_path_to_target(self):
        '''
        * Generates set directed graph with random weights
        * Checks correctness of algorithm to library's for 
          shortest path to target node
        '''
        g, nx_g = rand_graphs()

        bf_path = BF.bf_paths(g, 0, target=6)
        nx_path = nx.bellman_ford_path(nx_g, 0, 6)
        dj_path = Dijkstra.dij_paths(g, 0, t=6)
        dj_nx_path = nx.dijkstra_path(nx_g, 0, 6)

        self.assertListEqual(bf_path, nx_path)
        self.assertListEqual(dj_path, dj_nx_path)

    def test_path_to_all(self):
        '''
        * Generates set directed graph with random weights
        * Checks correctness of algorithm to library's for 
          shortest path to all nodes
        '''
        g, nx_g = rand_graphs()

        nx_paths = nx.single_source_bellman_ford_path(nx_g, 0)
        bf_paths = BF.bf_paths(g, 0)
        dj_paths = Dijkstra.dij_paths(g, 0)

        check = True
        for node in g:
            if nx_paths[node] != bf_paths[node] or nx_paths[node] != dj_paths[node]:
                check = False

        self.assertTrue(check)

    def test_graph_with_no_path(self):
        g = {0: [(1, 2)],
             1: [(2, 8), (3, 5)],
             2: [(3, -5)],
             3: [(5, -2), (6, 1)],
             4: [],
             5: [(6, 6)],
             6: []
        }
        nx_g = construct_nx_graph(g)

        with self.assertRaises(BF.NoPathError):
            BF.bellman_ford(g, 0, target=4)
        
        with self.assertRaises(Dijkstra.NoPathError):
            Dijkstra.dij(g, 0, t=4)

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
        with self.assertRaises(BF.NegativeCycleError):
            BF.bellman_ford(g, 0)

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
        with self.assertRaises(BF.NegativeCycleError):
            BF.bellman_ford(g, 0)



if __name__ == '__main__':
    unittest.main()