'''
dict to represent Graph:
    nodes == keys
    [(Edge to, Weight)] == Value

    a --> b (weight of 5)
    shown as 'a': [('b', 5)]
'''
import collections


def bellman_ford(graph, src, target=None):
    '''
    * Calculates shortest distances and previous nodes for each node

    :param graph: dict containing node: (edge, weight) pairs
                  represents the directed graph

    :param src: int representing the source node to start with

    :param target: Optional param giving target node to find shortest
                   distance to from src

    :return: None if negative cycle detected, else array with shortest 
             distances and paths is returned or shortest dist to target
             if target param is given  
    '''
    # List containing distances and previous node for shortest route
    d = [float('Inf') for v in graph]
    d[src] = 0

    # Loop through the graph finding the 
    # shortest paths with 'k' hops
    for k in range(1, len(graph) - 1):
        # Check for each vertex within the graph
        for v in graph:
            # Grab each edge connected to 'v' & their weight
            for u, w in graph[v]:
                # Update weight & previous node
                # if there's a shorter path
                dist_v = d[v]
                dist_u = d[u]
                if dist_v + w < dist_u:
                    d[u] = dist_v + w

    # Check for any negative cycles
    for v in graph:
        for u, w in graph[v]:
            # Check if 'n-th' hop creates a shorter dist
            dist_v = d[v]
            dist_u = d[u]
            if dist_v + w < dist_u:
                # print('Negative Cycle')
                return
    if target is not None:
        return d[target]
    
    return {node: d[node] for node in graph}

def construct_paths(graph, src):
    # List containing distances and previous node for shortest route
    d = [(float('Inf'), None) for v in graph]
    d[src] = (0, src)

    # Loop through the graph finding the 
    # shortest paths with 'k' hops
    for k in range(1, len(graph) - 1):
        # Check for each vertex within the graph
        for v in graph:
            # Grab each edge connected to 'v' & their weight
            for u, w in graph[v]:
                # Update weight & previous node
                # if there's a shorter path
                dist_v = d[v][0]
                dist_u = d[u][0]
                if dist_v + w < dist_u:
                    d[u] = (dist_v + w, v)

    # Check for any negative cycles
    for v in graph:
        for u, w in graph[v]:
            # Check if 'n-th' hop creates a shorter dist
            dist_v = d[v][0]
            dist_u = d[u][0]
            if dist_v + w < dist_u:
                # print('Negative Cycle')
                return
    
    return d

def bf_paths(graph, src, target=None):
    '''
    * Constructs shortest paths for every node in graph

    :param graph: dict containing (node: (edge, weight)) pairs
                  representing the directed graph
    
    :param src: int representing the source node to start with
    
    :return dict: Contains the shortest paths for each node in graph
                  if target is given, then returns shortest path from
                  src to target node
    '''
    # Get the shortest distances and previous node for each node
    d = construct_paths(graph, src)

    if d is None:
        return

    # Construct shortest path route
    shortest_paths = {node: [] for node in graph}

    for node in shortest_paths:
        path = collections.deque()
        path.append(node)
        prev = d[node][1]

        if prev == 0 and node != 0:
            path.appendleft(prev)
        elif node != 0:
            while prev != src:
                path.appendleft(prev)
                prev = d[prev][1]
            path.appendleft(src)

        shortest_paths[node] = list(path)

    if target is not None:
        return shortest_paths[target]

    return shortest_paths



if __name__ == '__main__':
    g = {0: [(1, 2)],
             1: [(2, 8), (3, 5)],
             2: [(3, -5)],
             3: [(4, 4), (5, -2), (6, 1)],
             4: [],
             5: [(6, 6)],
             6: []
        }

    print(bellman_ford(g, 0))
    print(bf_paths(g, 0))
    print(bellman_ford(g, 0, target=5))





