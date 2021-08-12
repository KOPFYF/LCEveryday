class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs, O(mn)/O(min(m, n))
        # Space complexity : O(min(M, N)) because in worst case where the grid is filled with lands, 
        # the size of queue can grow up to min(M,N).
        # thinking about level by level travese, each level contains purely '1'
        res = 0
        m, n = len(grid), len(grid[0])
        bfs = deque([])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    grid[x][y] = '0'
                    res += 1
                    bfs.append((x, y))
                    while bfs:
                        i, j = bfs.popleft()
                        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                bfs.append((nx, ny))
                                grid[nx][ny] = '0'
        return res
        
                    
        
        # dfs, O(mn)/O(mn)
        def dfs(x, y):
            grid[x][y] = '0'
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    dfs(nx, ny)
        
        res = 0
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    dfs(x, y)
                    res += 1
        return res
                    