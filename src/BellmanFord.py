'''
dict to represent Graph:
    nodes == keys
    [(Edge to, Weight)] == Value

    a --> b (weight of 5)
    shown as 'a': [('b', 5)]
'''



def bellman_ford(graph, src):
    '''
    :param graph: dict containing node: (edge, weight) pairs
                  represents the directed graph
    :param src: char representing the source node to start with
    :return: None if negative cycle detected, else array with shortest 
             paths is returned  
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
                print('Negative Cycle')
                return

    return d


if __name__ == '__main__':
    g = {0: [(1, 2)],
         1: [(2, 8), (3, 5)],
         2: [(3, -5)],
         3: []
    }

    print(bellman_ford(g, 0))





