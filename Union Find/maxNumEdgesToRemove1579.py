'''
Use spanning tree algoritm to choose from type3 edges first (Union Find): If two nodes are not from the same union, connect them
Then use type1 edges for Alice
Use type2 edges for Bob
Finnaly if they are still not connected, return -1
'''

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # run Union-Find three times
        # first on Type1, then on Type2 and Type3 simultaneously
        res = 0
        ua, ub = DSU(n + 1), DSU(n + 1)
        es = [[] for _ in range(4)]
        
        for edge in edges:
            es[edge[0]].append(edge)
            
        # type 3
        for t, u, v in es[3]:
            if not ua.isConnect(u, v):
                res += 1
                ua.union(u, v)
                ub.union(u, v)
        
        for t, u, v in es[2]:
            if not ua.isConnect(u, v):
                res += 1
                ua.union(u, v)
        
        for t, u, v in es[1]:
            if not ub.isConnect(u, v):
                res += 1
                ub.union(u, v)
                
        # if still not connected, return -1
        x = ua.find(1)
        if any(x != ua.find(i) for i in range(1, n + 1)):
            return -1
            
        x = ub.find(1)
        if any(x != ub.find(i) for i in range(1, n + 1)):
            return -1
        
        return len(edges) - res
            

class Solution2:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2, ans = UnionFindSet(n), UnionFindSet(n), 0
        
        for t, u, v in edges:
            if t != 3:
                continue
            if not uf1.union(u - 1, v - 1) or not uf2.union(u - 1, v - 1):
                ans += 1
        
        for t, u, v in edges:
            if t == 1 and not uf1.union(u - 1, v - 1):
                ans += 1
            elif t == 2 and not uf2.union(u - 1, v - 1):
                ans += 1
   
        return ans if uf1.size == n and uf2.size == n else -1

        
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