class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        seen = defaultdict(int)
        for x, y in edges:
            graph[x].add(y)
        
        def dfs(node):
            # return True if no cycle
            # 0: unvisited, 1: visited, -1: visiting
            if seen[node] == 1:
                return True
            if seen[node] == -1:
                return False
            if len(graph[node]) == 0: # reach end
                return node == destination
            seen[node] = -1
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            seen[node] = 1
            return True
        
        return dfs(source)