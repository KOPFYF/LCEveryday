class Solution1:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        hq = [(0, start[0], start[1])]
        seen = {tuple(start) : 0}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while hq:
            dist, x, y = heapq.heappop(hq)
            if x == destination[0] and y == destination[1]:
                return dist
            for dx, dy in dirs:
                nx, ny, d = x, y, 0 # mind the init settings here
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx+dx][ny+dy] != 1:
                    nx += dx
                    ny += dy
                    d += 1
                # after while loop, pos still valid, not on wall 
                if (nx, ny) not in seen or dist + d < seen[(nx, ny)]:
                    seen[(nx, ny)] = dist + d
                    heapq.heappush(hq, (dist + d, nx, ny))
        return -1

class Solution2(object):
    def shortestDistance(self, M, start, end):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        # Heap
        m, n = len(M), len(M[0])
        seen = {tuple(start) : 0}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dq = [(0, start[0], start[1])]
        while dq:
            dist, x, y = heapq.heappop(dq)
            if x == end[0] and y == end[1]:
                return dist
            for dx, dy in dirs:
                nx, ny, d = x + dx, y + dy, 1
                while 0 <= nx < m and 0 <= ny < n and M[nx][ny] != 1:
                    nx += dx; ny += dy; d += 1
                # backwards one step because we are on the wall now
                nx -= dx; ny -= dy; d -= 1
                if (nx, ny) not in seen or d + dist < seen[(nx, ny)]:
                    heapq.heappush(dq, (d + dist, nx, ny))
                    seen[(nx, ny)] = d + dist
        return -1