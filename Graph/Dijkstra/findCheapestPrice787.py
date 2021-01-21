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
  
        # 1 HEAP
        minheap = [(0, src, K + 1)] 
        
        while minheap:
            # (current total price, current source city, max distance to destination)
            cost, st, n = heapq.heappop(minheap)
            if st == dst:
                return cost
            if n > 0:
                for child, nxt_cost in graph[st]:
                    heapq.heappush(minheap, (cost+nxt_cost, child, n-1))
        return -1

        #2 BFS
        q = collections.deque()
        q.append((src, 0, 0)) #(cur node, steps, cost)
        ans = float('inf') # min cost
        while q:
            cur, stops, cost = q.popleft()
            if cur == dst:
                ans = min(ans, cost)
                continue
            
            if stops <= K and cost <= ans:
                for nxt_city, nxt_cost in graph[cur]:
                    q.append((nxt_city, stops+1, cost+nxt_cost))
        return ans if ans != float('inf') else -1

            