class DSU:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parents[px] = py

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
        
        dic = defaultdict(int)
        for i in range(n):
            dic[dsu.find(i)] += 1
        
        res = 0
        for cnt in dic.values():
            res += cnt * (n - cnt) 
        
        return res // 2