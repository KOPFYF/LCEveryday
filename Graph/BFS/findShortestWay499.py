class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # Heap + BFS
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

class Solution2:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        q, stopped = [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            if [x, y] == hole:
                return pattern
            for i, j, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    if [newX, newY] == hole:
                        break
                if (newX, newY) not in stopped or [dist + d, pattern + p] < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))
        return "impossible"


class Solution3_bug:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # BFS
        m, n = len(maze), len(maze[0])
        q, stopped = [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            if [x, y] == hole:
                return pattern
            for dx, dy, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                nx, ny, d = x + dx, y + dy, 0
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] != 1:
                    if [nx, ny] == hole:
                        break
                    nx += dx
                    ny += dy
                    d += 1
                nx -= dx
                ny -= dy
                # print(nx, ny, stopped, q)
                if (nx, ny) not in stopped or [dist + d, pattern + p] < stopped[(nx, ny)]:
                    stopped[(nx, ny)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, nx, ny))
        return "impossible"