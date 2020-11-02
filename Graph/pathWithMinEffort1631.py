class Solution1(object):
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
        # heapq.heapify(heap)
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
            
class Solution2(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """    
        # min of max, should consider binary search + BFS, 
        # Time: O(m * n * log(max)) 4400 ms, space: O(m * n)
        # given threshold k, check if possible using only edges of ≤ k cost.
        def isPath(effort):
            seen, dq = {(0, 0)}, deque([(0, 0)])
            while dq:
                x, y = dq.popleft()
                if (x, y) == (len(heights) - 1, len(heights[0]) - 1):
                    return True
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if len(heights) > r >= 0 <= c < len(heights[0]) and abs(heights[r][c] - heights[x][y]) <= effort and (r, c) not in seen:
                        seen.add((r, c))
                        dq.append((r, c))
            return False            
        
        lo, hi = 0, max(max(heights))
        while lo < hi:
            effort = lo + hi >> 1
            if isPath(effort):
                hi = effort
            else:
                lo = effort + 1
        return lo