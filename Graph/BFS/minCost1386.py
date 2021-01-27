class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # BFS O(mn)/O(mn)
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dq, seen = deque([(0, 0, 0)]), set()
        while dq:
            i, j, cost = dq.popleft()
            if (i, j) == (m-1, n-1): 
                return cost
            if (i, j) in seen:
                continue
            seen.add((i, j))
            for s, d in enumerate(dirs, 1):
                x, y = i + d[0], j + d[1]
                if m > x >= 0 <= y < n:
                    if s == grid[i][j]:
                        dq.appendleft((x, y, cost)) # like a heap
                    else:
                        dq.append((x, y, 1 + cost))