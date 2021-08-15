class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        def check_bfs(day):
            grid = [[0] * n for _ in range(m)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1  # Mark as water
            
            bfs = deque()
            for y in range(n):
                if grid[0][y] == 0:
                    bfs.append((0, y))
                    grid[0][y] = 1 # Mark as seen
            
            while bfs:
                x, y = bfs.popleft()
                if x == m - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        bfs.append((nx, ny))
                        grid[nx][ny] = 1
            return False
        
        l, r = 1, len(cells)
        res = 0
        while l < r:
            mid = (l + r) // 2
            if check_bfs(mid):
                res = mid
                l = mid + 1
            else:
                r = mid
        return res