class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        # sort based on cost (i.e. distance)
        edges.sort()
        # Kruskal's algorithm
        res = 0
        dsu = DSU(n)
        for cost, u, v in edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
                res += cost
        return res
        
        
class DSU(object):
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x: # if x is not root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)