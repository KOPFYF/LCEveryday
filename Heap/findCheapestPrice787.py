class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # build graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Dijkstra with heap, O(n^2logn) / O(n^2)
        pq = [(0, src, K + 1)] # cost, node, stops
        while pq:
            cost, cur, stops = heapq.heappop(pq)
            if cur == dst:
                return cost
            if stops > 0:
                for nxt, weight in graph[cur]:
                    heapq.heappush(pq, (cost + weight, nxt, stops - 1)) 
        return -1
        
            