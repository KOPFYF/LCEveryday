class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
            
        def dijkstra(city):
            hq = [(0, city)]
            dist = {} # seen
            
            while hq:
                d, u = heapq.heappop(hq)
                if u in dist: 
                    continue # pruning
                if u != city: 
                    dist[u] = d
                for v, w in graph[u].items():
                    if v not in dist and d + w <= distanceThreshold:
                        heapq.heappush(hq, (d + w, v))
            return len(dist)
        
        return max([(dijkstra(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]
                        
                        
                    