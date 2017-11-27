import heapq
import collections


class NoPathError(Exception):
    pass



def dij(adjacentList, s, t=None):
    infinity = float('inf')    
    PQ = []
    X = {x:x for x in adjacentList}
    prev = {x:x for x in adjacentList}
    distances = {x:infinity for x in adjacentList}
    distances[s] = 0
    item = [s, distances[s]]
    heapq.heappush(PQ, item)#insert (s,0) into PQ

    for n in X: 
        item = [n, infinity]
        heapq.heappush(PQ, item)#insert each node with distance infinity

    #for i = 0 in len(X):
    while(PQ):#not like his code!!!!
        v = heapq.heappop(PQ) #extractmin
        vNode = v[0]
        vDist = v[1]
        for u in adjacentList[vNode]: #nested for loop
            uNode = u[0]
            uvDist = u[1]

            if distances[uNode] > distances[vNode] + uvDist: #decreasekeypart
                distances[uNode] = distances[vNode] + uvDist #update the distance
                item = [uNode, distances[uNode]]
                heapq.heappush(PQ, item)
                prev[uNode] = vNode #updating previous list

    if t is not None:
        if distances[t] == infinity: #no path to t 
            raise NoPathError()
        else:
            return distances[t]
    
    return distances
    
def dij_paths(adjacentList, s, t=None):
    infinity = float('inf')    
    PQ = []
    paths = []
    X = {x:x for x in adjacentList}
    prev = {x:x for x in adjacentList}
    distances = { x:infinity for x in adjacentList}
    distances[s] = 0
    item = [s, distances[s]]
    heapq.heappush(PQ, item)#insert (s,0) into PQ

    for n in X: 
        item = [n, infinity]
        heapq.heappush(PQ, item)#insert each node with distance infinity

    
    #for i = 0 in len(X):
    while(PQ):#not like his code!!!!
        v = heapq.heappop(PQ) #extractmin
        vNode = v[0]
        vDist = v[1]
        
        for u in adjacentList[vNode]: #nested for loop
            uNode = u[0]
            uvDist = u[1]

            if distances[uNode] > distances[vNode] + uvDist: #decreasekeypart
                distances[uNode] = distances[vNode] + uvDist #update the distance
                item = [uNode, distances[uNode]]
                heapq.heappush(PQ, item)
                prev[uNode] = vNode

    if t is not None:
        return shortest_path(s, t, prev)
    
    # Construct shortest path route
    shortest_paths = {node: [] for node in adjacentList}

    for node in shortest_paths:
        try:
            shortest_paths[node] = shortest_path(s, node, prev)
        except NoPathError:
            pass
    
    return shortest_paths

def shortest_path(s, t, prev):
    # Collections.deque() used for O(1) insertion @ front of list
    path = collections.deque()

    path.append(t)
    prev_node = prev[t]

    if prev_node == t and t != 0:
        raise NoPathError()

    if prev_node == 0 and t != 0:
        path.appendleft(prev_node)
        return list(path)
    elif t != 0:
        curr_node = t
        while prev_node != s:
            if prev_node == curr_node:
                raise NoPathError()
            
            path.appendleft(prev_node)
            curr_node = prev_node
            prev_node = prev[prev_node]
            
        path.appendleft(s)
        
    return list(path)
        
def main():
     
    adj = {'a': [('b', 9), ('c', 6), ('e', 13)],
         'b': [('a', 9), ('f', 10)],
         'c': [('a', 6), ('e', 8), ('f', 18), ('d', 30)],
         'd': [('c', 30), ('e', 20), ('f', 6), ('h', 16), ('g', 11)],
         'e': [('a', 13), ('h', 25), ('c', 8), ('d', 20)],
         'f': [('b', 10), ('c', 18), ('d', 6),  ('g', 6), ('h', 19)],
         'g': [('d', 11), ('f', 6), ('h', 6)],
         'h': [('e', 25), ('f', 19), ('d', 16),  ('g', 6)]}

 
    dij_paths(adj, 'a', 'h')

if __name__ == "__main__":
    main()
