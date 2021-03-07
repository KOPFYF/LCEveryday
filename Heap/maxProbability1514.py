class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph, seen = defaultdict(dict), {start: -1}
        for (u, v), prob in zip(edges, succProb):
            graph[u][v] = prob 
            graph[v][u] = prob 
            
        hq = [(-1, start)]
        while hq:
            p, node = heapq.heappop(hq)
            if node == end: return -p
            
            for nxt in graph[node]:
                if nxt not in seen or seen[nxt] > p * graph[node][nxt]:
                    heapq.heappush(hq, (p * graph[node][nxt], nxt))
                    seen[nxt] = p * graph[node][nxt]
        return 0.0