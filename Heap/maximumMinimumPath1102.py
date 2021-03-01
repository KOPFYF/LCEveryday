class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # heap + BFS
        m, n = len(A), len(A[0])
        heap = [(-A[0][0], 0, 0)]
        seen = set([(0, 0)])
        
        while heap:
            val, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return -val
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    tmp = max(val, -A[nx][ny])
                    heapq.heappush(heap, (tmp, nx, ny))
        return -1