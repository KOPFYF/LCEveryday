class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        sx, sy = entrance[0], entrance[1]
        seen = set((sx, sy))
        
        bfs = deque([(sx, sy, 0)]) # x, y, step
        while bfs:
            x, y, d = bfs.popleft()
            if x in (0, m-1) or y in (0, n-1):
                if maze[x][y] == '.' and (x, y) != (sx, sy):
                    return d
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and \
                    maze[nx][ny] == '.' and (nx, ny) not in seen:
                    bfs.append((nx, ny, d + 1))
                    seen.add((nx, ny))
                    
        return -1