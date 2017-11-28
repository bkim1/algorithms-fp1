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

def gen_rand_graph(n, m=None, neg_weight=False):
    if m is not None:
        nx_g = nx.gnm_random_graph(n, m, directed=True)    
    else:
        nx_g = nx.gnm_random_graph(n, n, directed=True)

    g = {node: [] for node in nx_g}

    for u, v in nx_g.edges:
        if neg_weight:
            w = rand_weight(start=-5)
            if w == 0: 
                w -= 1
        else:
            w = rand_weight()
        g[u].append((v, w))
        nx_g.edges[u, v]['weight'] = w
    return (g, nx_g)

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

    return g, construct_nx_graph(g)

def rand_graphs_3(neg_weight=False):
    '''Constructs set directed graph with random weights with a graph 
    that has 16 nodes with set edges but randomized weights

    Returns:
        dict representing graph
    '''
    g = {0: [(1, rand_weight(start=-5))],
         1: [(2, rand_weight()), (6, rand_weight())],
         2: [(3, rand_weight(-20, 0))],
         3: [(4, rand_weight(-10)), (6, rand_weight(-4, 0))],
         4: [(5, rand_weight(-9))],
         5: [(6, rand_weight()), (11, rand_weight(-10))],
         6: [(7, rand_weight(-8)), (8, rand_weight()), (10, rand_weight())],
         7: [(9, rand_weight(-10,0))],
         8: [(9, rand_weight(-7)), (12, rand_weight())],
         9: [(10, rand_weight(-4)), (12, rand_weight()), (15, rand_weight(-4))],
         10: [(11, rand_weight(-10))],
         11: [(13, rand_weight())],
         12: [(13, rand_weight(-10,0))],
         13: [(14, rand_weight())],
         14: [(15, rand_weight())],
         15: []
    }

    return g

def rand_weight(start=-20, end=20):
    '''Returns random weight for graph'''
    weight = random.randint(start, end)
    return weight if weight != 0 else weight - 1


for i in range(100):
    # g, nx_g = gen_rand_graph(10, neg_weight=True)
    g, nx_g = rand_graphs_2()
    while True:
        try:
            bf_dists = BF.bellman_ford(g, 0)
        except BF.NegativeCycleError:
            # g, nx_g = gen_rand_graph(10, neg_weight=True)
            g, nx_g = rand_graphs_2()
        else:
            break

    dij_dists = Dijkstra.dij(g, 0)
    # nx_dij_dists = nx.single_source_dijkstra_path_length(nx_g, 0)

    for node in bf_dists:
        if bf_dists[node] != dij_dists[node]:
            print('---- Graph #%i Results ----' % i)
            print('Bellman Ford: %s\n' % bf_dists)
            print('Dijkstra:     %s\n' % dij_dists)
            # print('NX Dijkstra:  %s\n' % nx_dij_dists)


g = {0: [(1, 5), (2, 1)],
     1: [(3, -5)],
     2: [(3, 1)],
     3: [(4, 1)],
     4: []
}

print(BF.bellman_ford(g, 0, target=4))
print(Dijkstra.dij(g, 0, t=4))