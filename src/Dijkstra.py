import heapq
import math
from sys import stdin, stdout

def dij(adjacentList, s, t=None):
    infinity = float('inf')    
    PQ = []
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
            prev[uNode] = vnode #updating previous list
            if distances[uNode] > distances[vNode] + uvDist: #decreasekeypart
                distances[uNode] = distances[vNode] + uvDist #update the distance
                item = [uNode, distances[uNode]]
                heapq.heappush(PQ, item)

    if t is not None:
        if distances[t] == infinity: #no path to t 
            break
        else:
            return distances[t]
    else:
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
            prev[uNode] = vnode #updating previous list
            if distances[uNode] > distances[vNode] + uvDist: #decreasekeypart
                distances[uNode] = distances[vNode] + uvDist #update the distance
                item = [uNode, distances[uNode]]
                heapq.heappush(PQ, item)

    if t is not None:
        return prev[:t]
            
    else:
        return prev
            
        
def main():
     
    adj = {'a': [('b', 9), ('c', 6), ('e', 13)],
         'b': [('a', 9), ('f', 10)],
         'c': [('a', 6), ('e', 8), ('f', 18), ('d', 30)],
         'd': [('c', 30), ('e', 20), ('f', 6), ('h', 16), ('g', 11)],
         'e': [('a', 13), ('h', 25), ('c', 8), ('d', 20)],
         'f': [('b', 10), ('c', 18), ('d', 6),  ('g', 6), ('h', 19)],
         'g': [('d', 11), ('f', 6), ('h', 6)],
         'h': [('e', 25), ('f', 19), ('d', 16),  ('g', 6)]}

 
    dij(adj, 'a', 'h')

if __name__ == "__main__":
    main()
