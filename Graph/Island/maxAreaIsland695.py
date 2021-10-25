class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(grid, x, y):
            if not grid[x][y]:
                return 0
            res = 1
            grid[x][y] = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    res += dfs(grid, nx, ny)
            return res
        
        max_area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    max_area = max(dfs(grid, x, y), max_area)
        return max_area


class Solution1:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        
        def dfs(x, y):
            if (0 <= x < n) and (0 <= y < m) and grid[x][y]:
                grid[x][y] = 0
                return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) + 1
            return 0
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))
    
        return max_area