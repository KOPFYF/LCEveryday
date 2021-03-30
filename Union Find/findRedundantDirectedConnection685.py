'''
a. There is no cycle in the graph, but there exist two edges pointing to the same node;
b. There is a cycle, but there do not exist two edges pointing to the same node;
c. There is a cycle, and there exist two edges pointing to the same node.
'''
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        cand1, cand2, point_to = None, None, {} # hash table to record the edge
        for u, v in edges: 
            # u -> v
            if v in point_to:
                cand1, cand2 = point_to[v], [u, v] # currently, v has two indegree
                break # such node would be at most one
            point_to[v] = [u, v]
        
        dsu = DSU(len(edges))
        for u, v in edges:
            if [u, v] == cand2: 
                # loop to the second candidate
                continue
                # return cand2
            if dsu.isConnect(u - 1, v - 1): 
                # find a cycle
                if cand1: # case b
                    return cand1
                return [u, v] # case c
            else:
                dsu.union(u - 1, v - 1)
        return cand2
                

            
                        
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)