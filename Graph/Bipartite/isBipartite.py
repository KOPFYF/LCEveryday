class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(cur, color):
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