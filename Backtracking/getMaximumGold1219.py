class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or not grid[x][y]:
                return 0
            org, tmp = grid[x][y], 0
            grid[x][y] = 0 # marked as visited
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                tmp = max(tmp, dfs(nx, ny))
            grid[x][y] = org # give it back
            return grid[x][y] + tmp
        
        return max(dfs(x, y) for x in range(m) for y in range(n))