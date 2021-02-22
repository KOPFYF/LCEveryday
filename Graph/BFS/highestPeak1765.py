class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # BFS
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        bfs = deque([])
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    bfs.append((i, j))
                    height[i][j] = 0 # set water to zero
        
        while bfs:
            x, y = bfs.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    bfs.append((nx, ny))
        return height