class Solution(object):
    def pacificAtlantic(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # reverse engineering, start from borders and go up
        m = len(M)
        if not M or m == 0: return []
        n = len(M[0])
        
        p_visited = [[False for _ in range(n)] for _ in range(m)]   
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []
        
        def dfs(i, j, visited):
            visited[i][j] = True
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or M[x][y] < M[i][j]:
                    continue
                dfs(x, y, visited)
                
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n - 1, a_visited)
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m - 1, j, a_visited)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result