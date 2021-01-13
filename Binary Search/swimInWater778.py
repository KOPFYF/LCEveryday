class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # binary search O(n^2logn)
        n = len(grid)
        def check(t):
            # O(V + E), ~ O(n^2)
            bfs = deque([(0, 0)])
            seen = set((0, 0))
            while bfs:
                x, y = bfs.popleft()
                if grid[x][y] <= t:
                    if x == y and y == n - 1: return True
                    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen:
                            bfs.append((nx, ny))
                            seen.add((nx, ny))
            return False
        
        l, r = grid[0][0], n ** 2 - 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l