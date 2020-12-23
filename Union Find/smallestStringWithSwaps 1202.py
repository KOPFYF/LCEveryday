class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
        res = []
        d = defaultdict(list)
        for u, v in pairs:
            dsu.union(u, v)
        for i in range(n):
            d[dsu.find(i)].append(s[i])
        for comp_id in d.keys(): 
            d[comp_id].sort(reverse=True)
        # print(d)
        # find the lowest possible character that can be exchanged
        for i in range(n): 
            res.append(d[dsu.find(i)].pop()) # each char use once
        return ''.join(res)
            

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