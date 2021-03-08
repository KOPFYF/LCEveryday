class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # BFS, O(n^2)/O(n)
        # Put all land cells into a queue as source nodes and BFS for water cells, the last expanded one will be the farthest.
        n = len(grid)
        bfs = deque([])
        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    bfs.append((i, j, 0))
                    seen.add((i, j))
        if len(bfs) in (0, n * n):
            return -1
        res = 0
        while bfs:
            x, y, d = bfs.popleft()
            res = max(res, d)
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                    bfs.append((nx, ny, d + 1))
                    seen.add((nx, ny))
        return res
                    