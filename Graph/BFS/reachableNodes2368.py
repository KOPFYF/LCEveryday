class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # dfs, O(V+E)/O(V+E)
        def dfs(node: int) -> None:
            if node not in seen:
                seen.add(node)
                for nxt_node in g[node]:
                    dfs(nxt_node)
    
        seen = set(restricted)
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)        
        dfs(0)
        return len(seen) - len(restricted)  
    
        # bfs, O(V+E)/O(V+E)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bfs = deque([0])
        seen = set([0] + restricted)
        cnt = 1
        
        while bfs:
            node = bfs.popleft()
            for nxt_node in graph[node]:
                if nxt_node not in seen:
                    bfs.append(nxt_node)
                    seen.add(nxt_node)
                    cnt += 1
        
        return cnt