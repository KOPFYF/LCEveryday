class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        dsu = DSU(N)
        for t, u, v in sorted(logs):
            if not dsu.isConnect(u, v):
                dsu.union(u, v)
                if dsu.cnt == 1:
                    return t
        return -1
               
class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        self.cnt = N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr
        self.cnt -= 1
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)