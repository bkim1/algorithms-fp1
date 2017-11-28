# Implementation of the Bellman Ford shortest paths algorithm 
#
# Main functions:
#     1) bellman_ford() --> Returns shortest distances
#     2) bf_paths() --> Returns shortest paths
#
# Graph representation:
#     Use dict datastructure to represent Graph:
#         nodes == keys
#         [(Edge to, Weight)] == Value
#     Example:
#         1 --> 2 (weight of 5)
#         represented as (1: [(2, 5)])
import collections

class NoPathError(Exception):
    '''Exception for when there is no path from source to node'''
    pass

class NegativeCycleError(Exception):
    '''Exception for when there is a negative cycle in graph'''
    pass


def bellman_ford(graph, src, target=None):
    '''Calculates shortest distances for each node from a source
    
    Arguments:
        graph -- dict containing (node: (edge, weight)) pairs
                 represents the directed graph
        src -- int representing the source node to start with
        target -- Optional param giving target node to find shortest 
                  distance from src
    Return:
        None if negative cycle detected or graph is None, 
        Else dict with shortest distances for all nodes or shortest 
        distance to target if target param is given  
    Raises:
        ValueError -- if src or target are not valid nodes
        TypeError -- if src & target aren't ints or graph is not a dict
        NoPathError -- if there is no path to target node  
        NegativeCycleError -- if there is a negative cycle in the graph
    '''
    if graph is None:
        return None
    if type(graph) != dict:
        raise TypeError('Graph input must be a dictionary')
    if not isinstance(src, int):
        raise TypeError('Expected: int Got: %s' % (type(src)))
    if target is not None and not isinstance(target, int):
        raise TypeError('Expected: int Got: %s' % (type(target)))
   
    # List containing distances and previous node for shortest route
    # Initializing distance array taken from pseudo-code
    d = [float('Inf') for v in graph]
    try:
        d[src] = 0
    except IndexError:
        raise ValueError('src argument not a valid node')

    # Loop through the graph finding the shortest paths with 'k' hops
    # Code taken from pseudo-code
    for k in range(1, len(graph) - 1):
        # Check for each vertex within the graph
        for v in graph:
            # Grab each edge connected to 'v' & their weight
            for u, w in graph[v]:
                # Update weight & prev node if there's a shorter path
                if d[v] + w < d[u]:
                    d[u] = d[v] + w

    # Check for any negative cycles
    # Code taken from pseudo-code
    for v in graph:
        for u, w in graph[v]:
            # Check if 'n-th' hop creates a shorter dist
            if d[v] + w < d[u]:
                # Negative Cycle found!
                raise NegativeCycleError()
    
    if target is not None:
        try:
            if d[target] == float('Inf'):
                raise NoPathError()
        except IndexError:
            raise ValueError('target argument not a valid source')
    
        return d[target]
    
    return {node: d[node] for node in graph}


def bf_paths(graph, src, target=None):
    '''Constructs shortest paths for every node in graph based on 
    shortest distances unless a target node is specified

    Arguments:
        graph -- dict containing (node: (edge, weight)) pair 
                 representing the directed graph
        src -- int representing the source node to start with
    Return:
        dict with the shortest paths for each node in graph if target 
        is None, else list with shortest path from src to target node
    Raises:
        TypeError -- if src & target aren't ints or graph is not a dict
        NoPathError -- if there is no path to target node  
        NegativeCycleError -- if there is a negative cycle in the graph
    '''
    if graph is None:
        return None
    if type(graph) != dict:
        raise TypeError('Graph input must be a dictionary')
    if not isinstance(src, int):
        raise TypeError('Expected: int Got: %s' % (type(src)))
    if target is not None and not isinstance(target, int):
        raise TypeError('Expected: int Got: %s' % (type(target)))

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
    '''Construct the shortest path from source to target node with
    given list of previous nodes

    Arguments:
        src -- int representing the source node
        target -- int representing the target node
        path_list -- list with previous node for each node in graph
    Return:
        list containing the path from source to target node
    Raises:
        NoPathError -- if there is no path to target node  
    '''
    # Collections.deque() used for O(1) insertion @ front of list
    path = collections.deque()
    path.append(target)

    try:
        prev = path_list[target][1]
    except IndexError:
        raise ValueError('target argument not a valid node') 

    if prev is None:
        raise NoPathError()

    # Check if path is only the target and the source
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
        try:
            path.appendleft(src)
        except IndexError:
            raise ValueError('src argument not a valid node') 

    return list(path)


def construct_paths(graph, src):
    '''Runs Bellman Ford keeping track of previous nodes for each node

    Arguments:
        graph -- dict containing (node: (edge, weight)) pair 
                 representing the directed graph
        src -- int representing the source node to start with
    Return:
        list containing the distances and previous node for each node
    Raises:
        ValueError -- if src is not a valid node
        NegativeCycleError -- if there is a negative cycle in the graph
    '''
    # List containing distances and previous node for shortest route
    # Initializing distance array taken from pseudo-code
    d = [(float('Inf'), None) for v in graph]
    try:
        d[src] = (0, src)
    except IndexError:
        raise ValueError('src argument not a valid node')

    # Loop through the graph finding the shortest paths with 'k' hops
    # Code taken from pseudo-code
    for k in range(1, len(graph) - 1):
        # Check for each vertex within the graph
        for v in graph:
            # Grab each edge connected to 'v' & their weight
            for u, w in graph[v]:
                # Update weight & prev node if there's a shorter path
                dist_v = d[v][0]
                dist_u = d[u][0]
                if dist_v + w < dist_u:
                    d[u] = (dist_v + w, v)

    # Check for any negative cycles
    # Code taken from pseudo-code
    for v in graph:
        for u, w in graph[v]:
            # Check if 'n-th' hop creates a shorter dist
            dist_v = d[v][0]
            dist_u = d[u][0]
            if dist_v + w < dist_u:
                raise NegativeCycleError()
    
    return d


if __name__ == '__main__':
    g = {0: [(1, 3), (8, 20)],
         1: [(2, 1)],
         2: [(3, 7)],
         3: [(4, 5), (6, 10)],
         4: [(5, 2), (7, 6)],
         5: [(7, 3)],
         6: [(8, 1), (9, 6)],
         7: [(11, 15)],
         8: [(10, 4)],
         9: [(10, 11), (11, 5)],
         10: [(11, 8)],
         11: []
    }

    print(bellman_ford(g, 0))
    print(bf_paths(g, 0))
    print(bellman_ford(g, 0, target=11))
    print(bf_paths(g, 0, target=11))





