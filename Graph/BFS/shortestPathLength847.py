class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # BFS + bitmask (1 <= graph.length <= 12) O(n2^n)/O(n)
        # you may revisit nodes multiple times, and you may reuse edges.
        # seen will record(mask, node), aka same states can be reached from diff nodes 
        n = len(graph)
        seen, full_mask, q = set(), (1 << n) - 1, deque([(i, 0, 1 << i) for i in range(n)])
        while q:
            node, step, mask = q.popleft()
            if mask == full_mask: return step
            for v in graph[node]:
                if (mask | 1 << v, v) not in seen:
                    seen.add((mask | 1 << v, v))
                    q.append((v, step + 1, mask | 1 << v))
                            
        # heqpq + Bitmask (1 <= graph.length <= 12), O(nlogn2^n)/O(n)
        n = len(graph)
        seen, full_mask = set(), (1 << n) - 1
        # You may start and stop at any node, # (step, node, mask)
        hq = [(0, i, 1 << i) for i in range(n)] 
        while hq:
            step, node, mask = heapq.heappop(hq)
            if mask == full_mask: return step
            for v in graph[node]:
                if (mask | 1 << v, v) not in seen:
                    seen.add((mask | 1 << v, v))
                    heapq.heappush(hq, (step + 1, v, mask | 1 << v))
               
            
