class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # BFS
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        bfs = deque([(1, 1.0, 0)])
        # seen = set() # undirected graph, need to prevent going back
        seen = set([1])
        while bfs:
            node, prob, time = bfs.popleft()
            # seen.add(node)
            if time == t:
                if target == node:
                    return prob 
                continue # time ends and not see the target, return 0
            neighbors = graph[node] - seen
            if neighbors:
                for child in neighbors:
                    seen.add(child)
                    bfs.append((child, prob / len(neighbors), time + 1)) 
            else:
                # leaf nodes need to be pushed back to deque for next round
                bfs.append((node, prob, time + 1)) 
        return 0