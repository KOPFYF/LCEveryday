class Solution:
    def trapRainWater(self, M: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=cJayBq38VYw
        m, n, res, cur_max = len(M), len(M[0]), 0, 0
        seen = set((i, j) for i in range(m) for j in range(n) if i in (0, m - 1) or j in (0, n - 1))
        hq = [(M[i][j], i, j) for i in range(m) for j in range(n) if i in (0, m - 1) or j in (0, n - 1)]
        heapq.heapify(hq)
        while hq:
            h, x, y = heapq.heappop(hq)
            cur_max = max(cur_max, h) # update max when out of heap
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    if cur_max > M[nx][ny]:
                        res += (cur_max - M[nx][ny]) # acc when enter heap
                    heapq.heappush(hq, (M[nx][ny], nx, ny))
                    seen.add((nx, ny))
        return res