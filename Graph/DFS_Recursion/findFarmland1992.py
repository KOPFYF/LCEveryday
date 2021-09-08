class Solution_DFS:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        '''
        0: forested land
        1: farmland
        '''
        # O(mn) / O(mn)
        m, n = len(land), len(land[0]) # 1 <= m, n <= 300
        res = []
        
        # @lru_cache(None)
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and land[x][y] == 1:
                nx, ny = x, y
                land[x][y] = 0 # marked as visited
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = max((nx, ny), dfs(x + dx, y + dy))
                return nx, ny
            return 0, 0
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    res.append([i, j, x, y])
        return res


class Solution_BFS:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        visited = {}
        rows, cols = len(land), len(land[0])
        
        def bfs(i, j):
            q = deque([(i, j)])
            max_i, max_j = i, j
            while q:
                i, j = q.popleft()
                max_i, max_j = max(max_i, i), max(max_j, j)
                for a, b in ((0, 1), (1, 0)):
                    u, v = i + a, j + b
                    if 0 <= u <= rows - 1 and 0 <= v <= cols - 1 and land[u][v] and (u, v) not in visited:
                        visited[(u, v)] = 1
                        q.append((u, v))
            return max_i, max_j
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] and (i, j) not in visited:
                    visited[(i, j)] = 1
                    x, y = bfs(i, j)
                    res.append([i, j, x, y])
        return res