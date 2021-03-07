class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # O(ElogE + E^2)
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[2]) # O(ElogE)
        
        # do not use this edge
        def find_mst_without_this_edge(edge_idx):
            # O(E)
            dsu = DSU(n)
            res = 0
            for j, (u, v, w, _) in enumerate(edges):
                if j == edge_idx:
                    continue
                if not dsu.isConnect(u, v):
                    dsu.union(u, v)
                    res += w
            parent = dsu.find(0)
            return res if all(dsu.find(i) == parent for i in range(n)) else float('inf')
        
        # use this edge
        def find_mst_with_this_edge(edge_idx):
            # O(E)
            dsu = DSU(n)
            u0, v0, w0, _ = edges[edge_idx]
            res = w0
            dsu.union(u0, v0) # use this edge first
            for j, (u, v, w, _) in enumerate(edges):
                if j == edge_idx:
                    continue
                if not dsu.isConnect(u, v):
                    dsu.union(u, v)
                    res += w
            parent = dsu.find(0)
            return res if all(dsu.find(i) == parent for i in range(n)) else float('inf')
        
        # O(E^2)
        base = find_mst_without_this_edge(-1) # why -1?
        critial, pseudo = set(), set()
        for i in range(len(edges)):
            wgt_exclude = find_mst_without_this_edge(i)
            # if not included, MST total weight would increase
            if wgt_exclude > base: # this edge is a critical edge.
                critial.add(edges[i][-1])
            else:
                wgt_include = find_mst_with_this_edge(i)
                # with this edge, MST total weight doesn't change
                if wgt_include == base:
                    pseudo.add(edges[i][-1])
        
        return [critial, pseudo]
        
        
        
class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
        self.cnt = n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if not self.isConnect(x, y):
            self.parents[self.find(x)] = self.find(y)
            self.cnt -= 1
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)