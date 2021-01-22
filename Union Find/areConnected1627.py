class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # O(nlogn + q)/O(n)
        # N + N/2 + N/3 + ... + 1 = N * (1/N + 2/N + ... + 1) = N * 𝐻𝑛
        # 𝐻𝑛 ≈ 𝑙𝑛(𝑛)+γ and γ is the famous Euler - Mascheroni constant
        # "connect" all nodes that share common divisors into groups 
        # connect nodes 2, 4, 6, etc., then - 3, 6, 9, etc. 
        # If a node is already connected, we can skip it.
        uf = DSU(n + 1)
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i): # step by i
                if i > threshold:
                    uf.union(i, j)
        res = []
        for q in queries:
            pa = uf.find(q[0])
            pb = uf.find(q[1])
            res.append(pa == pb)
        return res
    
             
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