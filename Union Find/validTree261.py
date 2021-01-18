class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Number of edges = Number of nodes - 1
        if len(edges) + 1 != n: 
            return False
        dsu = DSU(n, n)
        for u, v in edges:
            # if u, v connected before, find a cycle!
            if dsu.find(u) == dsu.find(v):
                return False
            # otherwise, union u & v
            dsu.union(u, v)
        return True
               
        
class DSU(object):
    # Union by size
    def __init__(self, n, cnt):
        self.parents = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parents[i] = i
        self.count = cnt # add a count here!
        
    
    def find(self, x):
        # Path compression
        if self.parents[x] != x: # if x is nott root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        if self.size[rootx] <= self.size[rooty]:
            self.parents[rootx] = rooty
            self.size[rooty] += self.size[rootx]
        else:
            self.parents[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        # if union success, cnt -= 1
        self.count -= 1