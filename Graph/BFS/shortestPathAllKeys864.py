class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # BFS, O(m*n*2^k)
        m, n = len(grid), len(grid[0])
        numofKeys, seen = 0, set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j] in 'abcdef':
                    numofKeys += 1
        
        bfs = deque([(start[0], start[1], 0, ".@abcdef", 0)])
        while bfs:
            # canMove means the cells we can walk over
            i, j, steps, canMove, collectedKeys = bfs.popleft()
            if grid[i][j] in "abcdef" and grid[i][j].upper() not in canMove:
                # add 'ABCDEF' as not blocked cells
                canMove += grid[i][j].upper()
                collectedKeys += 1
            
            if collectedKeys == numofKeys: return steps
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] in canMove:
                    if (nx, ny, canMove) not in seen:
                        # we may visit a point more than one times
                        # so set seen stores canMove as well
                        seen.add((nx, ny, canMove)) 
                        bfs.append((nx, ny, steps + 1, canMove, collectedKeys))
        return -1
                        
