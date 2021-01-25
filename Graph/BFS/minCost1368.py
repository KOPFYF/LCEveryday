class Solution:
    def minCost(self, grid: List[List[int]]) -> int:           
        # BFS, O(mn)/O(mn)
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dq, costs = deque([(0, 0, 0)]), {}
        
        while dq:
            nx, ny, cost = dq.popleft()
            while 0 <= nx < m and 0 <= ny < n and (nx, ny) not in costs:
                costs[nx, ny] = cost
                dx1, dy1 = dirs[grid[nx][ny]-1]
                dq += [(nx+dx, ny+dy, cost+1) for (dx, dy) in dirs if (dx, dy) != (dx1, dy1)]
                nx, ny = nx+dx1, ny+dy1
        return costs[m-1, n-1]