class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        # BFS
        # grid[x][y]'s cell number is x * n + y
        # Traverse the cell's 4 neighbors:
        # a) if its neighbor is of different color, the cell is on the component border;
        # b) if same color, put the neighbor into Queue;
        org_color = grid[r0][c0]
        m, n = len(grid), len(grid[0])
        bfs = deque([(r0, c0)])
        seen = set([(r0, c0)])
        while bfs:
            x, y = bfs.popleft()
            if x * y * (m - x - 1) * (n - y - 1) == 0: # border
                grid[x][y] = color
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                    if grid[nx][ny] == org_color:
                        seen.add((nx, ny))
                        bfs.append((nx, ny))
                    else:  # neighbor is of different color
                        grid[x][y] = color
        return grid
        
        
        
        
        # perform DFS and flip the cell color to negative to track visited cells
        # After DFS is complete for the cell, check if this cell is inside. If so, flip its color back to the positive
        org_color = grid[r0][c0]
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            grid[x][y] = -org_color # marked as visited
            cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cnt += abs(grid[nx][ny]) == org_color # neighbor could be visited
                    if grid[nx][ny] == org_color:
                        dfs(nx, ny)
            if cnt == 4:
                grid[x][y] = org_color # set inner back to original color
        
        dfs(r0, c0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    grid[i][j] = color
        return grid

                
                    
                
            