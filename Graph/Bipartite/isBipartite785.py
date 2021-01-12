class Solution_DFS(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(cur, color):
            if colors[cur] != 0: # visited
                return colors[cur] == color
            
            colors[cur] = color
            for i in graph[cur]:
                if not dfs(i, -color): # try paint nxt
                    return False
            return True
        
        def dfs2(cur, color):
            colors[cur] = color # color current node
            for i in graph[cur]:
                # 1. if any neighbor is already colored with the same color. return False
                if colors[i] == color: 
                    return False
                # 2. ignore neighbors already colored with oppsite color;
                if colors[i] == -color:
                    continue
                # 3. if not visited, paint neighbors with opposite color, and recursively search
                if colors[i] == 0 and not dfs(i, -color): 
                    return False
            # return true if we can paint all nodes
            return True
            
        N = len(graph)    
        colors = [0] * N # 0 is not visited, 1/-1 are two colors to paint
        for i in range(N):
            if colors[i] == 0 and not dfs(i, -1): 
                return False
        return True

class Solution_BFS(object):
    def isBipartite(self, graph):
        # BFS
        n = len(graph)    
        colored = {} # 0 is not visited, 1/-1 are two colors to paint
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                q = deque([i])
                while q:
                    cur = q.popleft()
                    for nxt in graph[cur]:
                        if nxt not in colored:
                            colored[nxt] = -colored[cur]
                            q.append(nxt)
                        elif colored[nxt] == colored[cur]:
                            return False
        return True