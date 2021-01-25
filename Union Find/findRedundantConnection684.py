class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node_set = set()
        for u, v in edges:
            node_set.add(u)
            node_set.add(v)
        n = len(node_set)
        dsu = DSU(n + 1)
        for u, v in edges:
            if not dsu.isConnect(u, v):
                dsu.union(u, v)
            else:
                return [u, v]
                  
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