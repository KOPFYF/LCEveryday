'''

Dijkstra's shortest path algorithm is O(ElogV) where:

V is the number of vertices
E is the total number of edges
Your analysis is correct, but your symbols have different meanings! You say the algorithm is O(VElogV) where:

V is the number of vertices
E is the maximum number of edges attached to a single node.
Let's rename your E to N. So one analysis says O(ElogV) and another says O(VNlogV). 
Both are correct and in fact E = O(VN). The difference is that ElogV is a tighter estimation.

'''

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # O(ElogV)
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        
        # cache dist when node is pushed into the heap   
        # when cached, it's not guranteed to be the optimal, so dist could be updated
        def dijkstra2(city):
            # O(ElogV)
            hq = [(0, city)]
            dist = {city:0} # seen
            
            while hq:
                d, u = heapq.heappop(hq)
                for v, w in graph[u].items():
                    if (v not in dist or dist[v] > d + w) and d + w <= distanceThreshold:
                        heapq.heappush(hq, (d + w, v))
                        dist[v] = d + w
            return len(dist)

        return max([(dijkstra(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]

        # cache dist when node is popped out of the heap  
        # when popped out, the dist is guranteed to be the optimal/smallest  
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
                        
                        
