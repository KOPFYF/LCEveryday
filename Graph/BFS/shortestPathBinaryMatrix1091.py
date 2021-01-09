class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]: return -1
        
        bfs = deque([(0, 0, 1)])
        seen = set([(0, 0)])
        while bfs:
            x, y, step = bfs.popleft()
            if x == n - 1 and y == n - 1:
                return step 
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue 
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny] and (nx, ny) not in seen:
                        bfs.append((nx, ny, step + 1))
                        seen.add((nx, ny))
        return -1