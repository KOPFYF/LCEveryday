class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # case 1: There is a loop in the graph, and no vertex has more than 1 parent.
        # case 2: A vertex has more than 1 parent, but there isn't a loop in the graph.
        # case 3; A vertex has more than 1 parent, and is part of a loop.
        # https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases
        n = len(edges)
        dsu = DSU(n + 1)
        hasFather = [False] * (n + 1)
        self.graph = defaultdict(list)
        criticalEdge, cycleEdge = None, None
        
        for i, (u, v) in enumerate(edges):
            self.graph[u].append(v)
            # If a vertex has more than one parent, record the last edge
            if hasFather[v]:
                criticalEdge = [u, v]
            hasFather[v] = True
            # If a loop is found, record the edge that occurs last
            if dsu.isConnect(u, v):
                cycleEdge = [u, v]
            else:
                dsu.union(u, v)
        
        if not criticalEdge: return cycleEdge # Case 1
        self.visited = [False] * (n + 1)
        (u, v) = self.detectCycle(criticalEdge[1])
        return (u, v) if u else criticalEdge # Case 2 and 3
            
    def detectCycle(self, V):
        self.visited[V] = True
        for i in range(len(self.graph[V])):
            nextV = self.graph[V][i]
            if self.visited[nextV]:
                return (V, nextV)
            res = self.detectCycle(nextV)
            if res[0]:
                return res
        return (None, None)
            
                        
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)



class Solution2:
    def findRedundantDirectedConnection(self, edges):
        def find(u):  # union find
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        
        def detect_cycle(edge):  # check whether you can go from u to v (forms a cycle) along the parents 
            u, v = edge
            while u != v and u in parents:
                u = parents[u]
            return u == v
        
        candidates = []  # stores the two edges from the vertex where it has two parents
        parents = {}
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append((parents[v], v)) 
                candidates.append((u, v))
           
        if candidates:  # case 2 & case 3 where one vertex has two parents
            return candidates[0] if detect_cycle(candidates[0]) else candidates[1]
        else:  # case 1, we just perform a standard union find, same as redundant-connection
            p = list(range(len(edges)))
            for edge in edges:
                u, v = map(find, edge)
                if u == v:
                    return edge
                p[u] = p[v]