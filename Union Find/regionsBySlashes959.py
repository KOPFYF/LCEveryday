class DSU:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)
        
class Solution_uf:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(4 * n * n)
        for i in range(n):
            for j in range(n):
                root = 4 * (n * i + j)
                if grid[i][j] in "/ ":
                    dsu.union(root, root + 1)
                    dsu.union(root + 2, root + 3)
                if grid[i][j] in "\\ ":
                    dsu.union(root, root + 2)
                    dsu.union(root + 1, root + 3)
                if i > 0:
                    dsu.union(root, root + 3 - 4 * n)
                if i < n - 1:
                    dsu.union(root + 3, root + 4 * n)
                if j > 0:
                    dsu.union(root + 1, root - 2)
                if j < n - 1:
                    dsu.union(root + 2, root + 5)
        return sum(dsu.find(x) == x for x in range(n * n * 4))


class Solution_bfs:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        # Transform every '/' or '\' into an upscaled 1:3 grid
        # then it becomes number of island
        n = len(grid) * 3
        G = [[True] * n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                # print(char)
                if char == '/':
                    G[3 * i][3 * j + 2] = False
                    G[3 * i + 1][3 * j + 1] = False
                    G[3 * i + 2][3 * j] = False
                elif char == '\\':
                    G[3 * i][3 * j] = False
                    G[3 * i + 1][3 * j + 1] = False
                    G[3 * i + 2][3 * j + 2] = False
        # BFS
        cnt, seen = 0, set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(n):
                if G[i][j] and (i, j) not in seen:
                    cnt += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        seen.add((x, y))
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen and G[nx][ny]:
                                stack.append((nx, ny))
        return cnt