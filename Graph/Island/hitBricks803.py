# https://leetcode.com/problems/bricks-falling-when-hit/discuss/119829/Python-Solution-by-reversely-adding-hits-bricks-back

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # start from the last hit to the first hit
        # For each hit (i, j), if grid[i][j]==0, set grid[i][j]=-1 otherwise set grid[i][j]=0
        # For i in [0, n], do dfs at grid[i][0] and mark no-dropping bricks
        # For each hit (i,j) (reversely), 
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            # how many bricks are connected to this stable one?
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            cnt = 1
            grid[i][j] = 2 # visited, stable
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = dx + i, dy + j
                cnt += dfs(x, y)
            return cnt
        
        def isConnected(i, j):
            # Check whether (i, j) is connected to Not Falling Bricks
            return i == 0 or any([0<=x<m and 0<=y<n and grid[x][y]==2 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]])
        
        for i, j in hits:
            grid[i][j] -= 1
        
        for i in range(n):
            dfs(0, i)
        
        res = [0] * len(hits)
        for k, (i, j) in enumerate(hits[::-1]):
            grid[i][j] += 1 # recover the hit
            if grid[i][j] == 1 and isConnected(i, j):
                # if (i, j) is a brick and it's connected to the top
                res[k] = dfs(i, j) - 1 # exclude itself
            
        return res[::-1]