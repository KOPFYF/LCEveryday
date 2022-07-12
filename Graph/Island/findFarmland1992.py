class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        
        def dfs(i, j):
            # return the bottom right coordinate
            if i < 0 or i >= m or j < 0 or j >= n or land[i][j] == 0:
                return (0, 0)
            
            land[i][j] = 0 # mark as seen
            
            i1, j1 = dfs(i + 1, j)
            i2, j2 = dfs(i, j + 1)
            
            return (max(i1, i2, i), max(j1, j2, j))
        
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    r, c = dfs(i, j)
                    res.append([i, j, r, c])
        
        return res