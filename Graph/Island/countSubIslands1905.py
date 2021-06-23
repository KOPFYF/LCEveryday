class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x, y):
            # return True if (x, y) island from grid2 is a sub-island
            grid2[x][y] = 0
            res = grid1[x][y]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny]:
                    res &= dfs(nx, ny)
            return res
          
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and dfs(i, j):
                    ans += 1
        return ans