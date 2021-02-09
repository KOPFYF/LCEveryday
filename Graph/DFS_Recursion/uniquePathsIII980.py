class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # DFS
        self.res, empty = 0, 1
        # empty=1 cause the starting square is counted besides the squares with a value of 0.
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    x, y = i, j
                elif grid[i][j] == 0: 
                    empty += 1
                    
        def dfs(x, y, empty):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0: return
            
            if grid[x][y] == 2:
                self.res += (empty == 0)
                return
            
            grid[x][y] = -2 # marked as visited
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, empty - 1)
            grid[x][y] = 0 # set it back
        
        dfs(x, y, empty)
        return self.res