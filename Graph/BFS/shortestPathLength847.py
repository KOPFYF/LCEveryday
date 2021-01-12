class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # BFS with Deque + bitmask, O(n*(2**n))
        memo, final, q = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))
        
        # level-by-level BFS + bitmask
        # BFS will guarantee shortest path because it will check every possible moves in each step
        # newstate = state | 1 << v
        # Why can't we just use the state?
        # This is because same states can be reached from different nodes too. So we must store the node too in the tuple.
        memo, final, steps = set(), (1 << len(graph)) - 1, 0
        q = [(i, 1 << i) for i in range(len(graph))]
        while True:
            new = []
            for node, state in q:
                if state == final: 
                    return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1
            
        # Heapq + bitmask
        memo, final, q = set(), (1 << len(graph)) - 1, [(0, i, 1 << i) for i in range(len(graph))]
        while q:
            steps, node, state = heapq.heappop(q)
            if state == final: 
                return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    heapq.heappush(q, (steps + 1, v, state | 1 << v))
                    memo.add((state | 1 << v, v))