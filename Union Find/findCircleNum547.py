class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # soln 1
        n = len(M)
        res = n
        dsu = DSU(n)
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    if not dsu.find(i) == dsu.find(j): 
                        # i & j are not in the same group yet
                        dsu.union(i, j)
                        res -= 1 # every time we do a valid union we decrease 1
        return res
        
        # soln 2
        n = len(M)
        dsu = DSU(n)
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    dsu.union(i, j)
        res = 0
        for i in range(n):
            if dsu.find(i) == i:
                res += 1
        return res
        
        
class DSU(object):
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)
        
        
        