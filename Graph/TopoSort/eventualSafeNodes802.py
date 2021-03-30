class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        seen = defaultdict(int)
        def dfs(node):
            # return True if no cycle
            # -1 visiting, 1 visited
            if seen[node] == 1:
                return True
            if seen[node] == -1:
                return False
            seen[node] = -1
            for nxt_node in graph[node]:
                if not dfs(nxt_node):
                    return False
            
            seen[node] = 1
            return True
        
        res = []
        for node in range(len(graph)):
            if dfs(node):
                res.append(node)
        return res