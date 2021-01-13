class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for i, j, k in flights:
            graph[i].append((j, k))

        #2 BFS
        q = collections.deque()
        q.append((src, 0, 0)) #(cur node, steps, cost)
        ans = float('inf') # min cost
        while q:
            cur, stops, cost = q.popleft()
            if cur == dst:
                ans = min(ans, cost) # bfs need min() here
                continue # once arrive at dst, it might not be the best soln so continue
            
            if stops <= K and cost <= ans:
                for nxt_city, nxt_cost in graph[cur]:
                    q.append((nxt_city, stops+1, cost+nxt_cost))
        return ans if ans != float('inf') else -1