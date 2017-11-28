import unittest
import random
import networkx as nx
import src.BellmanFord as BF
import src.Dijkstra as Dijkstra

def construct_nx_graph(g):
    '''Constructs the directed graph using the NetworkX library and 
    adds all nodes, edges, and weights from input dict

    Argument:
        g -- input dictionary representing graph
    Returns:
        NetworkX's directed graph with same nodes, edges, and weights
    '''
    dg = nx.DiGraph()

    for node in g:
        dg.add_node(node)

    for node in g:
        for edge, weight in g[node]:
            dg.add_edge(node, edge, weight=weight)

    return dg

def rand_graphs():
    '''Constructs set directed graph with random weights with a graph 
    that has 7 nodes with set edges but randomized weights

    Returns:
        dict representing graph and a NetworkX version
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
    '''Constructs set directed graph with random weights with a graph 
    that has 12 nodes with set edges but randomized weights

    Returns:
        dict representing graph and a NetworkX version
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
    '''Constructs set directed graph with random weights with a graph 
    that has 16 nodes with set edges but randomized weights

    Returns:
        dict representing graph and a NetworkX version
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
    '''Returns random weight for graph'''
    return random.randint(start, end)

class TestAlg(unittest.TestCase):
    def test_dist_to_target(self):
        '''Generates directed graph with random weights and checks
        correctness vs. NetworkX's algorithm
        '''
        g, nx_g = rand_graphs()

        nx_dist = nx.bellman_ford_path_length(nx_g, 0, 6)
        bf_dist = BF.bellman_ford(g, 0, target=6)
        dj_dist = Dijkstra.dij(g, 0, t=6)

        self.assertEqual(nx_dist, bf_dist)
        self.assertEqual(dj_dist, nx_dist)

    def test_dist_to_target_100(self):
        '''Generates 100 random directed graphs and tests correctness
        for the shortest distance from a source to a target node
        '''
        check = True

        # Test graph setup #1
        for _ in range(34):
            g, nx_g = rand_graphs()
            nx_dist = nx.bellman_ford_path_length(nx_g, 0, 6)
            bf_dist = BF.bellman_ford(g, 0, target=6)
            dj_dist = Dijkstra.dij(g, 0, t=6)

            if nx_dist != bf_dist or nx_dist != dj_dist:
                check = False
                break

        self.assertTrue(check)
        # Test graph setup #2
        for _ in range(33):
            g, nx_g = rand_graphs_2()
            nx_dist = nx.bellman_ford_path_length(nx_g, 0, 11)
            bf_dist = BF.bellman_ford(g, 0, target=11)
            dj_dist = Dijkstra.dij(g, 0, t=11)

            if nx_dist != bf_dist  or nx_dist != dj_dist:
                check = False
                break
        
        self.assertTrue(check)

        # Test graph setup #3
        for _ in range(33):
            g, nx_g = rand_graphs_3()
            nx_dist = nx.bellman_ford_path_length(nx_g, 0, 15)
            bf_dist = BF.bellman_ford(g, 0, target=15)
            dj_dist = Dijkstra.dij(g, 0, t=15)

            if nx_dist != bf_dist  or nx_dist != dj_dist:
                check = False
                break

        self.assertTrue(check)

    def test_dist_to_all(self):
        '''Generates directed graph with random weights and checks
        correctness vs. NetworkX's algorithm
        '''
        g, nx_g = rand_graphs()

        nx_dists = nx.single_source_bellman_ford_path_length(nx_g, 0)
        bf_dists = BF.bellman_ford(g, 0)
        dj_dists = Dijkstra.dij(g, 0)

        check = True
        for node in g:
            if nx_dists[node] != bf_dists[node] or nx_dists[node] != dj_dists[node]:
                check = False

        self.assertTrue(check)

    def test_dist_to_all_100(self):
        '''Generates 100 random directed graphs and tests correctness
        for the shortest distance from a source to all nodes
        '''
        check = True

        # Test graph setup #1
        for _ in range(34):
            g, nx_g = rand_graphs()
            nx_dists = nx.single_source_bellman_ford_path_length(nx_g, 0)
            bf_dists = BF.bellman_ford(g, 0)
            dj_dists = Dijkstra.dij(g, 0)

            check = True
            for node in g:
                if nx_dists[node] != bf_dists[node] or nx_dists[node] != dj_dists[node]:
                    check = False
                    break
        
        self.assertTrue(check)

        # Test graph setup #2
        for _ in range(33):
            g, nx_g = rand_graphs_2()
            nx_dists = nx.single_source_bellman_ford_path_length(nx_g, 0)
            bf_dists = BF.bellman_ford(g, 0)
            dj_dists = Dijkstra.dij(g, 0)

            check = True
            for node in g:
                if nx_dists[node] != bf_dists[node] or nx_dists[node] != dj_dists[node]:
                    check = False
                    break
        
        self.assertTrue(check)
        
        # Test graph setup #3
        for _ in range(33):
            g, nx_g = rand_graphs_3()
            nx_dists = nx.single_source_bellman_ford_path_length(nx_g, 0)
            bf_dists = BF.bellman_ford(g, 0)
            dj_dists = Dijkstra.dij(g, 0)

            check = True
            for node in g:
                if nx_dists[node] != bf_dists[node] or nx_dists[node] != dj_dists[node]:
                    check = False
                    break

        self.assertTrue(check)
    
    def test_path_to_target(self):
        '''Generates directed graph with random weights and checks
        correctness vs. NetworkX's algorithm
        '''
        g, nx_g = rand_graphs()

        bf_path = BF.bf_paths(g, 0, target=6)
        nx_path = nx.bellman_ford_path(nx_g, 0, 6)
        dj_path = Dijkstra.dij_paths(g, 0, t=6)

        self.assertListEqual(bf_path, nx_path)
        self.assertListEqual(dj_path, nx_path)

    def test_path_to_target_100(self):
        '''Generates 100 random directed graphs and tests correctness
        for the shortest path from a source to a target node
        '''
        check = True

        # Test graph setup #1
        for _ in range(34):
            g, nx_g = rand_graphs()
            bf_path = BF.bf_paths(g, 0, target=6)
            nx_path = nx.bellman_ford_path(nx_g, 0, 6)
            dj_path = Dijkstra.dij_paths(g, 0, t=6)

            if nx_path != bf_path or nx_path != dj_path:
                check = False
                break

        self.assertTrue(check)

        # Test graph setup #2
        for _ in range(33):
            g, nx_g = rand_graphs_2()
            bf_path = BF.bf_paths(g, 0, target=11)
            nx_path = nx.bellman_ford_path(nx_g, 0, 11)
            dj_path = Dijkstra.dij_paths(g, 0, t=11)

            if nx_path != bf_path or nx_path != dj_path:
                check = False
                break
        
        self.assertTrue(check)

        # Test graph setup #3
        for _ in range(33):
            g, nx_g = rand_graphs_3()
            bf_path = BF.bf_paths(g, 0, target=15)
            nx_path = nx.bellman_ford_path(nx_g, 0, 15)
            dj_path = Dijkstra.dij_paths(g, 0, t=15)

            if nx_path != bf_path or nx_path != dj_path:
                check = False
                break

        self.assertTrue(check)

    def test_path_to_all(self):
        '''Generates directed graph with random weights and checks
        correctness vs. NetworkX's algorithm
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

    def test_path_to_all_100(self):
        '''Generates 100 random directed graphs and tests correctness
        for the shortest path from a source to all nodes
        '''
        check = True

        # Test graph setup #1
        for _ in range(34):
            g, nx_g = rand_graphs()
            nx_paths = nx.single_source_bellman_ford_path(nx_g, 0)
            bf_paths = BF.bf_paths(g, 0)
            dj_paths = Dijkstra.dij_paths(g, 0)

            check = True
            for node in g:
                if nx_paths[node] != bf_paths[node] or nx_paths[node] != dj_paths[node]:
                    check = False
                    break

        self.assertTrue(check)

        # Test graph setup #2
        for _ in range(33):
            g, nx_g = rand_graphs_2()
            nx_paths = nx.single_source_bellman_ford_path(nx_g, 0)
            bf_paths = BF.bf_paths(g, 0)
            dj_paths = Dijkstra.dij_paths(g, 0)

            check = True
            for node in g:
                if nx_paths[node] != bf_paths[node] or nx_paths[node] != dj_paths[node]:
                    check = False
                    break
        
        self.assertTrue(check)

        # Test graph setup #3
        for _ in range(33):
            g, nx_g = rand_graphs_3()
            nx_paths = nx.single_source_bellman_ford_path(nx_g, 0)
            bf_paths = BF.bf_paths(g, 0)
            dj_paths = Dijkstra.dij_paths(g, 0)

            check = True
            for node in g:
                if nx_paths[node] != bf_paths[node] or nx_paths[node] != dj_paths[node]:
                    check = False
                    break

        self.assertTrue(check)

    def test_empty_graph(self):
        '''Tests that Error is raised with empty graph'''
        with self.assertRaises(TypeError):
            test = BF.bellman_ford({},None)
        
    def test_invalid_src(self):
        #with self.assertRaises(ValueError):
        pass
            

    def test_graph_with_no_path(self):
        '''Tests that NoPathError is correctly raised'''
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
        '''Tests that NegativeCycleError is correctly raised'''
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
        '''Tests that NegativeCycleError is correctly raised'''
        g = {0: [(1, 2)],
             1: [(2, 8), (3, 5)],
             2: [(3, -5)],
             3: [(2, 2)]
        }
        with self.assertRaises(BF.NegativeCycleError):
            BF.bellman_ford(g, 0)



if __name__ == '__main__':
    unittest.main()