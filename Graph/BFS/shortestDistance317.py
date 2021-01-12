class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        M = [[[0, 0] for _ in range(n)] for _ in range(m)] # (hit, distSum)
        
        cnt = 0 # count how many building we have visited
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # bfs start from grid=1
                    self.bfs([i, j], grid, M, cnt, m, n)
                    cnt += 1
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if M[i][j][1] == cnt: # (i, j) can visit all buildings
                    res = min(res, M[i][j][0])
        return res if res != float('inf') else -1
    
    def bfs(self, start, grid, matrix, cnt, m, n):
        q = deque([(start, 0)])
        while q:
            tmp = q.popleft()
            po, step = tmp[0], tmp[1]
            for dp in [(-1,0), (1,0), (0,1), (0,-1)]:
                i, j = po[0] + dp[0], po[1] + dp[1]
                # only the position be visited by cnt times will append to queue
                if 0 <= i < m and 0 <= j < n and matrix[i][j][1] == cnt and grid[i][j] == 0:
                    matrix[i][j][0] += step + 1 # update shortest amount of distance
                    matrix[i][j][1] = cnt + 1 # update counts
                    q.append(([i,j], step + 1))


class Solution2:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        reach = [[0 for _ in range(cols)] for _ in range(rows)]
        dist = [[0 for _ in range(cols)] for _ in range(rows)]

        def bfs(i, j, cnt):
            queue = collections.deque([(i, j, 0)])
            while queue:
                r, c, step = queue.popleft()
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and reach[nr][nc] == cnt:
                        dist[nr][nc] += step + 1
                        reach[nr][nc] += 1
                        queue.append((nr, nc, step + 1))
                step += 1

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    bfs(i, j, cnt)
                    cnt += 1

        ans = float("inf")
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and reach[i][j] == cnt:
                    ans = min(ans, dist[i][j])

        return ans if ans < float("inf") else -1