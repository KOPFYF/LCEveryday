class Solution(object):
    def shortestDistance(self, M, start, end):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        
        # deque not work must use heap !!!
        # Time: O(m * n): worst case visit the entire matrix
        # Space: O(m * n): seen Matrix
#         m, n = len(M), len(M[0])
#         seen = [[-1] * n for _ in range(m)]
#         seen[start[0]][start[1]] = 0
#         dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]    
#         dq = deque([(start[0], start[1])])
    
#         while dq:
#             x, y = dq.popleft()
#             dist = seen[x][y]
#             if x == end[0] and y == end[1]:
#                 return dist
#             for dx, dy in dirs:
#                 nx, ny, d = x + dx, y + dy, 0
#                 while 0 <= nx < m and 0 <= ny < n and M[nx][ny] != 1:
#                     nx += dx
#                     ny += dy
#                     d += 1
#                 # backwards one step because we are on the wall now
#                 nx -= dx
#                 ny -= dy
#                 if seen[nx][ny] == -1 or dist + d < seen[nx][ny]:
#                     dq.append((nx, ny))
#                     seen[nx][ny] = dist + d
#         return -1
        
        # SSSP
        m, n = len(M), len(M[0])
        seen = [[-1] * n for _ in range(m)]
        seen[start[0]][start[1]] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        #dq = deque([(0, start[0], start[1])])
        dq = [(0, start[0], start[1])]
        while dq:
            dist, x, y = heapq.heappop(dq)
            if x == end[0] and y == end[1]:
                return dist
            for dx, dy in dirs:
                nx, ny, d = x + dx, y + dy, 0
                while 0 <= nx < m and 0 <= ny < n and M[nx][ny] != 1:
                    nx += dx
                    ny += dy
                    d += 1
                # backwards one step because we are on the wall now
                nx -= dx
                ny -= dy
                if seen[nx][ny] == -1 or dist + d < seen[nx][ny]:
                    heapq.heappush(dq, (dist + d, nx, ny))
                    seen[nx][ny] = dist + d
        return -1