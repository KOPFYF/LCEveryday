class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Time: O(ElogE + QlogQ). Where E is the number of edges in edgeList and Q is the number of queries. This comes from sorting both inputs.
        # Space: O(n). Where n is the number of nodes.
        res = [None] * len(queries)
        # Sort queries based on weight and sort edges based on weight as well
        edgeList.sort(key=lambda x: x[2]) # sort by weight
        queries = sorted([q + [i] for i, q in enumerate(queries)], key=lambda x: x[2])
        dsu = DSU(n)
        
        i = 0
        for a, b, limit, idx in queries:
            # traverse the edges that are smaller than the limit
            # Since we are visiting the queries with increasing limit
            # we just need to visit edges once from small distance to large distance.
            while i < len(edgeList) and edgeList[i][2] < limit:
                x, y, d = edgeList[i]
                dsu.union(x, y)
                i += 1
            # Check if nodes p and q are connected in Union-Find structure
            res[idx] = dsu.find(a) == dsu.find(b)   
            
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