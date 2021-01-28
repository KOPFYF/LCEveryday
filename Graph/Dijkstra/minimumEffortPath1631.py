class Solution1(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # Dijikstra(BFS) + heap, always pop the min d, update with max
        # Time: O(E log V), E = 4*m*n/2, V = m*n, Space O(V)
        # 860 ms, push, pop takes at most O(log mn), so time O(mnlog mn)
        if not heights: return 0
        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = {(0, 0): float('inf')}
        while heap:
            d, x, y = heapq.heappop(heap) 
            if (x, y) == (m - 1, n - 1): return d
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n:
                    nd = max(d, abs(heights[nx][ny] - heights[x][y]))
                    if (nx, ny) not in seen or seen[(nx, ny)] > nd:
                        heapq.heappush(heap, (nd, nx, ny))
                        seen[(nx, ny)] = nd


class Solution2(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # Dijikstra(BFS) + heap, always pop the min d, update with max
        # Time: O(E log V), E = 4*m*n/2, V = m*n, Space O(V)
        # 860 ms, push, pop takes at most O(log mn), so time O(mnlog mn)
        if not heights: 
            return 0
        m, n, res = len(heights), len(heights[0]), 0
        heap = [(0, 0, 0)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()    
        while heap:
            d, x, y = heapq.heappop(heap)
            res = max(d, res)
            seen.add((x, y))
            if (x, y) == (m - 1, n - 1): # end
                return res
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    nd = abs(heights[nx][ny] - heights[x][y])
                    heapq.heappush(heap, (nd, nx, ny))
        return res
            