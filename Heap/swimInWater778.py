class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # heap, O(n^2logn)
        n, res = len(grid), 0
        seen, pq = set((0, 0)), [(grid[0][0], 0, 0)]
        while pq:
            t, x, y = heapq.heappop(pq)
            res = max(res, t)
            if x == y == n - 1: return res
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))