# Benchmarks performance of our Bellman Ford and Dijkstra 
# implementations versus NetworkX's implementations
#
# Benchmark prompts user for number of times to run tests
#
# Compares:
#     - Our Bellman Ford vs. Our Dijkstra
#     - Our Bellman Ford vs. NetworkX's Bellman Ford
#     - Our Dijkstra vs. NetworkX's Dijkstra
#
# Outputs:
#     - Average times for each
#     - Minimum time for each
#     - Maximum time for each
#     - Percent difference for each comparison
import time
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


def test_dij(g, t):
    '''Returns time to run Dijkstra from src to target'''
    t0 = time.time()
    dist = Dijkstra.dij(g, 0, t=t)
    t1 = time.time()

    return t1 - t0

def test_bf(g, t):
    '''Returns time to run Bellman Ford from src to target'''
    t0 = time.time()
    dist = BF.bellman_ford(g, 0, target=t)
    t1 = time.time()

    return t1 - t0

def test_nx_dij(g, t):
    '''Returns time to run NetworkX Dijkstra from src to target'''
    t0 = time.time()
    dist = nx.dijkstra_path_length(g, 0, t)
    t1 = time.time()

    return t1 - t0

def test_nx_bf(g, t):
    '''Returns time to run NetworkX Bellman Ford from src to target'''
    t0 = time.time()
    dist = nx.bellman_ford_path_length(g, 0, t)
    t1 = time.time()

    return t1 - t0

'''  ---------  START OF BENCHMARKING ---------  '''

# Get number of times to run each test
while True:
    try:
        num_times = int(input('Number of times to run tests: '))
    except ValueError:
        print('Input must be a number')
    except KeyboardInterrupt:
        print()
        exit(0)
    else:
        if num_times > 0:
            break

print('----- Time to Find Shortest Distance From Source to Target -----\n')
print('Tests are run %i times each\n' % num_times)


print('----- Directed Graph #1 -----')
g, nx_g = rand_graphs()

bf_times = [test_bf(g, 6) for _ in range(num_times)]
dij_times = [test_dij(g, 6) for _ in range(num_times)]
nx_dij_times = [test_nx_dij(nx_g, 6) for _ in range(num_times)]
nx_bf_times = [test_nx_bf(nx_g, 6) for _ in range(num_times)]

bf_avg = sum(bf_times) / len(bf_times)
bf_min = min(bf_times)
bf_max = max(bf_times)

nx_bf_avg = sum(nx_bf_times) / len(nx_bf_times)
nx_bf_min = min(nx_bf_times)
nx_bf_max = max(nx_bf_times)

dij_avg = sum(dij_times) / len(dij_times)
dij_min = min(dij_times)
dij_max = max(dij_times)

nx_dij_avg = sum(nx_dij_times) / len(nx_dij_times)
nx_dij_min = min(nx_dij_times)
nx_dij_max = max(nx_dij_times)

print('Our BF       --> Average: %f Min: %f Max: %f' % (bf_avg, bf_min, bf_max))
print('Our Dij      --> Average: %f Min: %f Max: %f' % (dij_avg, dij_min, dij_max))
print('NetworkX BF  --> Average: %f Min: %f Max: %f' % (nx_bf_avg, nx_bf_min, nx_bf_max))
print('NetworkX Dij --> Average: %f Min: %f Max: %f' % (nx_dij_avg, nx_dij_min, nx_dij_max))

bf_dij_diff = ((max(dij_avg, bf_avg) - min(dij_avg, bf_avg))/min(dij_avg, bf_avg)) * 100
bf_nx_diff = ((max(nx_bf_avg, bf_avg) - min(nx_bf_avg, bf_avg))/min(nx_bf_avg, bf_avg)) * 100
dij_nx_diff = ((max(nx_dij_avg, dij_avg) - min(nx_dij_avg, dij_avg))/min(nx_dij_avg, dij_avg)) * 100
print('\nOur BF vs. Our Dij Percent Difference: %.2f%%' % bf_dij_diff)
print('Winner: %s' % ('BF' if bf_avg <= dij_avg else 'Dij'))

print('\nOur BF vs. NetworkX BF Percent Difference: %.2f%%' % bf_nx_diff)
print('Winner: %s' % ('Our BF' if bf_avg <= nx_bf_avg else 'NetworkX BF'))

print('\nOur Dij vs. NetworkX Dij Percent Difference: %.2f%%' % dij_nx_diff)
print('Winner: %s' % ('Our Dij' if dij_avg <= nx_dij_avg else 'NetworkX Dij'))


print('\n----- Directed Graph #2 -----')
g, nx_g = rand_graphs_2()

bf_times = [test_bf(g, 11) for _ in range(num_times)]
dij_times = [test_dij(g, 11) for _ in range(num_times)]
nx_dij_times = [test_nx_dij(nx_g, 11) for _ in range(num_times)]
nx_bf_times = [test_nx_bf(nx_g, 11) for _ in range(num_times)]

bf_avg = sum(bf_times) / len(bf_times)
bf_min = min(bf_times)
bf_max = max(bf_times)

nx_bf_avg = sum(nx_bf_times) / len(nx_bf_times)
nx_bf_min = min(nx_bf_times)
nx_bf_max = max(nx_bf_times)

dij_avg = sum(dij_times) / len(dij_times)
dij_min = min(dij_times)
dij_max = max(dij_times)

nx_dij_avg = sum(nx_dij_times) / len(nx_dij_times)
nx_dij_min = min(nx_dij_times)
nx_dij_max = max(nx_dij_times)

print('Our BF       --> Average: %f Min: %f Max: %f' % (bf_avg, bf_min, bf_max))
print('Our Dij      --> Average: %f Min: %f Max: %f' % (dij_avg, dij_min, dij_max))
print('NetworkX BF  --> Average: %f Min: %f Max: %f' % (nx_bf_avg, nx_bf_min, nx_bf_max))
print('NetworkX Dij --> Average: %f Min: %f Max: %f' % (nx_dij_avg, nx_dij_min, nx_dij_max))

bf_dij_diff = ((max(dij_avg, bf_avg) - min(dij_avg, bf_avg))/min(dij_avg, bf_avg)) * 100
bf_nx_diff = ((max(nx_bf_avg, bf_avg) - min(nx_bf_avg, bf_avg))/min(nx_bf_avg, bf_avg)) * 100
dij_nx_diff = ((max(nx_dij_avg, dij_avg) - min(nx_dij_avg, dij_avg))/min(nx_dij_avg, dij_avg)) * 100
print('\nOur BF vs. Our Dij Percent Difference: %.2f%%' % bf_dij_diff)
print('Winner: %s' % ('BF' if bf_avg <= dij_avg else 'Dij'))

print('\nOur BF vs. NetworkX BF Percent Difference: %.2f%%' % bf_nx_diff)
print('Winner: %s' % ('Our BF' if bf_avg <= nx_bf_avg else 'NetworkX BF'))

print('\nOur Dij vs. NetworkX Dij Percent Difference: %.2f%%' % dij_nx_diff)
print('Winner: %s' % ('Our Dij' if dij_avg <= nx_dij_avg else 'NetworkX Dij'))


print('\n----- Directed Graph #3 -----')
g, nx_g = rand_graphs_3()

bf_times = [test_bf(g, 15) for _ in range(num_times)]
dij_times = [test_dij(g, 15) for _ in range(num_times)]
nx_dij_times = [test_nx_dij(nx_g, 15) for _ in range(num_times)]
nx_bf_times = [test_nx_bf(nx_g, 15) for _ in range(num_times)]

bf_avg = sum(bf_times) / len(bf_times)
bf_min = min(bf_times)
bf_max = max(bf_times)

nx_bf_avg = sum(nx_bf_times) / len(nx_bf_times)
nx_bf_min = min(nx_bf_times)
nx_bf_max = max(nx_bf_times)

dij_avg = sum(dij_times) / len(dij_times)
dij_min = min(dij_times)
dij_max = max(dij_times)

nx_dij_avg = sum(nx_dij_times) / len(nx_dij_times)
nx_dij_min = min(nx_dij_times)
nx_dij_max = max(nx_dij_times)

print('Our BF       --> Average: %f Min: %f Max: %f' % (bf_avg, bf_min, bf_max))
print('Our Dij      --> Average: %f Min: %f Max: %f' % (dij_avg, dij_min, dij_max))
print('NetworkX BF  --> Average: %f Min: %f Max: %f' % (nx_bf_avg, nx_bf_min, nx_bf_max))
print('NetworkX Dij --> Average: %f Min: %f Max: %f' % (nx_dij_avg, nx_dij_min, nx_dij_max))

bf_dij_diff = ((max(dij_avg, bf_avg) - min(dij_avg, bf_avg))/min(dij_avg, bf_avg)) * 100
bf_nx_diff = ((max(nx_bf_avg, bf_avg) - min(nx_bf_avg, bf_avg))/min(nx_bf_avg, bf_avg)) * 100
dij_nx_diff = ((max(nx_dij_avg, dij_avg) - min(nx_dij_avg, dij_avg))/min(nx_dij_avg, dij_avg)) * 100
print('\nOur BF vs. Our Dij Percent Difference: %.2f%%' % bf_dij_diff)
print('Winner: %s' % ('BF' if bf_avg <= dij_avg else 'Dij'))

print('\nOur BF vs. NetworkX BF Percent Difference: %.2f%%' % bf_nx_diff)
print('Winner: %s' % ('Our BF' if bf_avg <= nx_bf_avg else 'NetworkX BF'))

print('\nOur Dij vs. NetworkX Dij Percent Difference: %.2f%%' % dij_nx_diff)
print('Winner: %s' % ('Our Dij' if dij_avg <= nx_dij_avg else 'NetworkX Dij'))