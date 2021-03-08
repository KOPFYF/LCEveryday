class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # The number of operations we need = the number of connected networks - 1
        if len(connections) < n - 1: return -1
        dsu = DSU(n)
        for u, v in connections:
            dsu.union(u, v)
        return dsu.cnt - 1
            
            
class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
        self.cnt = n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if not self.isConnect(x, y):
            self.parents[self.find(x)] = self.find(y)
            self.cnt -= 1
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)