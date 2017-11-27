'''
* Implementation of the Bellman Ford shortest paths algorithm 
* Two main methods:
    1) bellman_ford() --> Returns shortest distances
    2) bf_paths() --> Returns shortest paths

* dict to represent Graph:
    nodes == keys
    [(Edge to, Weight)] == Value

    1 --> 2 (weight of 5)
    respresented as (1: [(2, 5)])
'''
import collections

class NoPathError(Exception):
    pass

class NegativeCycleError(Exception):
    pass

def bellman_ford(graph, src, target=None):
    '''
    * Calculates shortest distances and previous nodes for each node

    :param graph: dict containing (node: (edge, weight)) pairs
                  represents the directed graph

    :param src: int representing the source node to start with

    :param target: Optional param giving target node to find shortest
                   distance to from src

    :return: None if negative cycle detected, else array with shortest 
             distances and paths is returned or shortest dist to target
             if target param is given  
    '''
    # List containing distances and previous node for shortest route
    # Initializing distance array taken from pseudo-code
    d = [float('Inf') for v in graph]
    d[src] = 0

    # Loop through the graph finding the shortest paths with 'k' hops
    # For loops taken from pseudo-code
    for k in range(1, len(graph) - 1):
        # Check for each vertex within the graph
        for v in graph:
            # Grab each edge connected to 'v' & their weight
            for u, w in graph[v]:
                # Update weight & previous node if there's a shorter path
                if d[v] + w < d[u]:
                    d[u] = d[v] + w

    # Check for any negative cycles
    # Both for loops taken from pseudo-code
    for v in graph:
        for u, w in graph[v]:
            # Check if 'n-th' hop creates a shorter dist
            if d[v] + w < d[u]:
                # Negative Cycle --> Return None
                raise NegativeCycleError()
    
    if target is not None:
        if d[target] == float('Inf'):
            raise NoPathError()
        return d[target]
    
    return {node: d[node] for node in graph}


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

    if target is not None:
        return shortest_path(src, target, d)

    for node in shortest_paths:
        try:
            shortest_paths[node] = shortest_path(src, node, d)
        except NoPathError:
            pass

    return shortest_paths

def shortest_path(src, target, path_list):
    '''
    * Helper method to construct the shortest path from source to target node
    '''
    # Collections.deque() used for O(1) insertion @ front of list
    path = collections.deque()

    path.append(target)
    prev = path_list[target][1]

    if prev is None:
        raise NoPathError()

    if prev == 0 and target != 0:
        path.appendleft(prev)
        return list(path)
    elif target != 0:
        # Loop through and append previous nodes to list
        while prev != src:
            if prev is None:
                raise NoPathError()
            # Append to front of list for order
            path.appendleft(prev)
            prev = path_list[prev][1]
        path.appendleft(src)

    return list(path)


def construct_paths(graph, src):
    '''
    * Helper method that runs Bellman Ford with paths
      using a previous node for each node
    '''
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
                raise NegativeCycleError()
    
    return d


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





