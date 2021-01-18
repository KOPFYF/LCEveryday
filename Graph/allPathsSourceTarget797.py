class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS, dont use a seen set() because multiple paths
        n = len(graph)
        res = []
        bfs = deque([(0, [0])])
        while bfs:
            cur, path = bfs.popleft()
            if cur == n - 1:
                res.append(path)
            for nxt in graph[cur]:
                bfs.append((nxt, path + [nxt]))
        return res
    
        # DFS
        def dfs(cur, path):
            if cur == len(graph) - 1: 
                res.append(path)
            else:
                for i in graph[cur]: 
                    dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res