class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # soln 2
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res
    
        # soln 1
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if not dsu.isConnect(u, v):
                res -= 1
                dsu.union(u, v)
        return res
    
class DSU(object):
    # Union by size
    def __init__(self, n):
        self.parents = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        # Path compression
        if self.parents[x] != x: # if x is nott root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return False
        if self.size[rootx] <= self.size[rooty]:
            self.parents[rootx] = rooty
            self.size[rooty] += self.size[rootx]
        else:
            self.parents[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        return True
            
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)