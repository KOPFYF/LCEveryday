class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        bfs, seen = deque([]), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    bfs.append((0, i, j))
                    seen.add((i, j))
                elif grid[i][j] == 'X':
                    seen.add((i, j))
        
        while bfs:
            step, x, y = bfs.popleft()
            if grid[x][y] == '#':
                return step
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    bfs.append((step + 1, nx, ny))
                    seen.add((nx, ny))
        return -1