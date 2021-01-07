class Solution(object):
    def findLatestStep(self, arr, m):
        n = len(arr)
        if m == n:
            return m
        res, dsu = -1, DSU(n)
        
        for step, i in enumerate(arr):
            i -= 1 # 1-indexed
            dsu.ranks[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if dsu.ranks[dsu.find(j)] == m:
                        res = step
                    if dsu.ranks[j]: # if group j not 0
                        dsu.union(i, j)
        return res
            
    
class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True
        