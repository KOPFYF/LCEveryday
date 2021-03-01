class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x, y, parent):
            # prevent visiting parent would make the cycle len >= 4
            if (x, y) in seen: 
                return True
            seen.add((x, y))
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]: 
                if 0 <= nx < m and 0 <= ny < n and grid[x][y] == grid[nx][ny] and (nx, ny) != parent:
                    if dfs(nx, ny, (x, y)): 
                        return True 
            return False  
    
        m, n = len(grid), len(grid[0])
        seen = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen: 
                    if dfs(i, j, None): 
                        return True
        return False 