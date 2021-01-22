class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # heap
        seen, graph = set(), defaultdict(dict)
        for u, v, w in pipes:
            graph[u][v] = graph[v][u] = min(graph[v].get(u, float('inf')), w)
        cost, undone, pq = 0, n, [(w, i) for i, w in enumerate(wells, 1)]
        heapq.heapify(pq)
        while pq:
            c, x = heapq.heappop(pq)
            if x not in seen:
                cost += c
                undone -= 1
                if not undone:
                    break
                seen.add(x)
                for y, w in graph[x].items():
                    if y not in seen:
                        heapq.heappush(pq, (w, y))
        return cost
        
        # Union find
        dsu = DSU(n + 1)
        # set 0 as water source that connected with each well
        total = [[0, i, w] for i, w in enumerate(wells,1)] + pipes
        # union by weight of edge
        cost, cnt = 0, n
        for u, v, w in sorted(total, key=lambda x:x[2]):
            if not dsu.isConnect(u, v):
                dsu.union(u, v)
                cost += w
                cnt -= 1
            if cnt == 0: # MST is bulit!
                break
        return cost


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
    
    