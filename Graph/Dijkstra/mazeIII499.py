class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        q, stopped = [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            if [x, y] == hole:
                return pattern
            for dx, dy, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                nx, ny, d = x, y, 0
                while 0 <= nx+dx < m and 0 <= ny+dy < n and not maze[nx + dx][ny + dy]:
                    nx += dx
                    ny += dy
                    d += 1
                    if [nx, ny] == hole:
                        break
                # print(nx, ny, stopped, q)
                if (nx, ny) not in stopped or [dist + d, pattern + p] < stopped[(nx, ny)]:
                    stopped[(nx, ny)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, nx, ny))
        return "impossible"