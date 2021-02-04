class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # DFS, O(mn)/O(mn)
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen_p, seen_a = set(), set()

        def dfs(x, y, seen):
            seen.add((x, y)) # make the code a little shorter
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and \
                (nx, ny) not in seen and matrix[nx][ny] >= matrix[x][y]:
                    dfs(nx, ny, seen)
        
        for i in range(m):
            dfs(i, 0, seen_p)
            dfs(i, n - 1, seen_a)
        for j in range(n):
            dfs(0, j, seen_p)
            dfs(m - 1, j, seen_a)
        
        return [[i, j] for i in range(m) for j in range(n) \
                if (i, j) in seen_p and (i, j) in seen_a]


class Solution2(object):
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