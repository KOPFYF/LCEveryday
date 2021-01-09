class Solution:
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