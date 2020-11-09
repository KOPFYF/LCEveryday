class Solution1(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS
        # Runtime: O(n * n). We process an individual cell only once (or twice).
        # Memory: O(n) for the queue.
        # Reverse thinking: start from all lands, run BFS and update max distance
        m, n, level = len(grid), len(grid[0]), 0
        dq = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(dq) == m * n or len(dq) == 0:
            return -1
        while dq:
            # since we discover steps/distances, we do BFS level by level
            for _ in range(len(dq)):
                x, y = dq.popleft()
                for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx< m and 0 <= ny <n and grid[nx][ny] == 0:
                        # if next step is water, marked as land
                        dq.append((nx, ny))
                        grid[nx][ny] = 1
            level += 1
        return level - 1 # return l - 1 because in the end +1 is redudant


class Solution2(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Runtime: O(m * n * n), where m is the number of land cells.
        # Memory: O(n * n) for the recursion. DFS failed on the last case
        m, n, res = len(grid), len(grid[0]), -1
        def dfs(x, y, d=1):
            if x < 0 or x >= m or y < 0 or y >= n or (grid[x][y] != 0 and grid[x][y] <= d):
                return
            grid[x][y] = d
            dfs(x + 1, y, d + 1)
            dfs(x - 1, y, d + 1)
            dfs(x, y + 1, d + 1)
            dfs(x, y - 1, d + 1)
            
        # remark 0 with distance
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    dfs(i, j, 1)   
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 2:
                    res = max(res, grid[i][j] - 1)
        return res 