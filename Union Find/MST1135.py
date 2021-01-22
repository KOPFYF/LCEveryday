class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int: 
        dsu = DSU(N + 1)
        # union by weight of edge
        cost, cnt = 0, N
        for u, v, w in sorted(connections, key=lambda x:x[2]):
            if not dsu.isConnect(u, v):
                dsu.union(u, v)
                cost += w
                cnt -= 1
            if cnt == 1: # MST is bulit! we have N - 1 edges/unions
                return cost
        return -1
        
             
class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if not self.isConnect(x, y):
            self.parents[self.find(x)] = self.find(y)
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)