class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # O(m * n * maxMove)/O(m * n * maxMove)
        @lru_cache(None)
        def dfs(x, y, move):
            if move > maxMove:
                return 0
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            
            res = 0
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                res += dfs(nx, ny, move + 1)
            return res % (10 ** 9 + 7)
        
        return dfs(startRow, startColumn, 0)