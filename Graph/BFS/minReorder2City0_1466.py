class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v in connections:
            graph[u][v] = 1 # cost 1
            graph[v][u] = 0
            
        res = 0
        seen = set([0])
        bfs = deque([0])
        
        # bfs search with reversed edge, if dir exists, + 1
        while bfs:
            cur = bfs.popleft()
            for nxt in graph[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    res += graph[cur][nxt]
                    bfs.append(nxt)
        
        return res