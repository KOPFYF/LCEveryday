class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
        
        '''
        m, n = len(grid), len(grid[0])
        bfs = deque() # (x, y, t)
        fresh_oranges, time = 0, 0
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    fresh_oranges += 1
                elif grid[x][y] == 2:
                    bfs.append((x, y, 0))
        
        while bfs:
            x, y, time = bfs.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    bfs.append((nx, ny, time + 1))
                    grid[nx][ny] = 2 # mark as seen
                    fresh_oranges -= 1
        
        return time if fresh_oranges == 0 else -1