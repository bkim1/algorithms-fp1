import csv
import time
import random
import networkx as nx
import src.BellmanFord as BF
import src.Dijkstra as Dijkstra

def gen_rand_graph(n, m=None):
    if m is not None:
        nx_g = nx.gnm_random_graph(n, m, directed=True)    
    else:
        nx_g = nx.gnm_random_graph(n, n, directed=True)

    g = {node: [] for node in nx_g}

    for u, v in nx_g.edges:
        w = rand_weight()
        g[u].append((v, w))
        nx_g.edges[u, v]['weight'] = w
    return (g, nx_g)

def rand_weight(start=1, end=20):
    '''Returns random weight for graph'''
    return random.randint(start, end)

def test_dij(g, t=None):
    '''Returns time to run Dijkstra from src to all nodes'''
    t0 = time.time()
    dist = Dijkstra.dij(g, 0)
    t1 = time.time()

    return t1 - t0

def test_bf(g, t=None):
    '''Returns time to run Bellman Ford from src to all nodes'''
    t0 = time.time()
    dist = BF.bellman_ford(g, 0)
    t1 = time.time()

    return t1 - t0

def test_nx_dij(g, t=None):
    '''Returns time to run NetworkX Dijkstra from src to all nodes'''
    t0 = time.time()
    dist = nx.single_source_dijkstra_path_length(g, 0)
    t1 = time.time()

    return t1 - t0

def test_nx_bf(g, t=None):
    '''Returns time to run NetworkX Bellman Ford from src to all nodes'''
    t0 = time.time()
    dist = nx.single_source_bellman_ford_path_length(g, 0)
    t1 = time.time()

    return t1 - t0

# g, nx_g = gen_rand_graph(1000, 47978)
# # print(g)
# # print(len(nx_g.nodes))
# # print(len(nx_g.edges))
# # print(nx_g.edges)

# # nx_dist = nx.single_source_bellman_ford_path_length(nx_g, 0)
# # bf_dist = BF.bellman_ford(g, 0)

# # print(nx_dist)
# # print(bf_dist)
# print(test_bf(g))
# print(test_nx_bf(nx_g))

# exit(0)

all_bf = []
all_dij = []
all_nx_bf = []
all_nx_dij = []

for n in range(2, 51):
    bf_times = []
    dij_times = []
    nx_bf_times = []
    nx_dij_times = []

    for _ in range(1000):
        g, nx_g = gen_rand_graph(n)
        
        while True:
            try:
                bf_times.append(test_bf(g, n-1))
            except BF.NoPathError:
                g, nx_g = gen_rand_graph(n)
            else:
                break
        
        dij_times.append(test_dij(g, n-1))
        nx_bf_times.append(test_nx_bf(nx_g, n-1))
        nx_dij_times.append(test_nx_dij(nx_g, n-1))
    
    all_bf.append(sum(bf_times) / len(bf_times))
    all_dij.append(sum(dij_times) / len(dij_times))
    all_nx_bf.append(sum(nx_bf_times) / len(nx_bf_times))
    all_nx_dij.append(sum(nx_dij_times) / len(nx_dij_times))

all_bf_str = ['%f' % val for val in all_bf]
all_dij_str = ['%f' % val for val in all_dij]
all_nx_bf_str = ['%f' % val for val in all_nx_bf]
all_nx_dij_str = ['%f' % val for val in all_nx_dij]

print('Outputting to file!')

with open('perf_output.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(all_bf_str)
    writer.writerow(all_dij_str)
    writer.writerow(all_nx_bf_str)
    writer.writerow(all_nx_dij_str)



    