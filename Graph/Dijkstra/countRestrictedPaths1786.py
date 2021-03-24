class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7 # take care!
        graph = defaultdict(dict)
        seen = {n: 0}
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        
        hq = [(0, n)]
        while hq:
            s, node = heapq.heappop(hq)
            for nxt in graph[node]:
                if nxt not in seen or seen[nxt] > s + graph[node][nxt]:
                    seen[nxt] = s + graph[node][nxt]
                    heapq.heappush(hq, (s + graph[node][nxt], nxt))

        @lru_cache(None)
        def dfs(src):
            if src == n: 
                return 1  # Find a path to reach to destination
            ans = 0
            for nei in graph[src]:
                if seen[src] > seen[nei]:
                    ans += dfs(nei)
            return ans

        ans = dfs(1)
        return ans % mod