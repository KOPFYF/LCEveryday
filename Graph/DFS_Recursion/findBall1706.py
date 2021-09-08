class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def dfs(y):
            for x in range(m):
                ny = y + grid[x][y] # ny +/-1, +1 means one step to the right
                if ny < 0 or ny >= n or grid[x][y] != grid[x][ny]:
                    # Must have the board direction as the same, otherwise dead end
                    return -1
                y = ny
            return y
        
        return map(dfs, range(n))