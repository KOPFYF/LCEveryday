class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        bfs = deque([(0, 0, 0)]) # x, y and obs so far
        seen = {(0, 0, 0)}
        steps = 0
        
        while bfs:
            size = len(bfs)
            for _ in range(size):
                x, y, obs = bfs.popleft()
                if obs > k:
                    continue # invalid soln
                if x == m-1 and y == n-1:
                    return steps
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            nxt_obs = obs + 1
                        else:
                            nxt_obs = obs
                        if (nx, ny, nxt_obs) not in seen:
                            seen.add((nx, ny, nxt_obs))
                            bfs.append((nx, ny, nxt_obs))
                
            steps += 1
        return -1


class Solution1:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        bfs = deque([(0, 0, 0, 0)]) # x, y and obs so far, and steps
        seen = {(0, 0, 0)}
        steps = 0
        
        while bfs:
            x, y, obs, steps = bfs.popleft()
            if obs > k:
                continue # invalid soln
            if x == m-1 and y == n-1:
                return steps
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        nxt_obs = obs + 1
                    else:
                        nxt_obs = obs
                    if (nx, ny, nxt_obs) not in seen:
                        seen.add((nx, ny, nxt_obs))
                        bfs.append((nx, ny, nxt_obs, steps + 1))
        return -1