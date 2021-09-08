class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                grid[x][y] = 1
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    dfs(nx, ny)
        
        # fill boundary 0 with 1 ahead
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i in (0, m - 1) or j in (0, n - 1)):
                    dfs(i, j)
        
        # the rest is # of island
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res