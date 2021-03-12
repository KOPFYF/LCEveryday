class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # BFS
        m, n = len(image), len(image[0])
        seen = set((sr, sc))
        bfs = deque([(sr, sc)])
        color = image[sr][sc]
        while bfs:
            x, y = bfs.popleft()
            image[x][y] = newColor
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if  0 <= nx < m and 0 <= ny < n and image[nx][ny] == color and (nx, ny) not in seen:
                    image[nx][ny] = newColor
                    bfs.append((nx, ny))
                    seen.add((nx, ny))
        return image
        
        # DFS
        m, n = len(image), len(image[0])
        seen = set((sr, sc))
        def dfs(x, y, color):
            image[x][y] = newColor
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == color and (nx, ny) not in seen:
                    image[nx][ny] = newColor
                    seen.add((nx, ny))
                    dfs(nx, ny, color)
                        
        dfs(sr, sc, image[sr][sc])
        return image