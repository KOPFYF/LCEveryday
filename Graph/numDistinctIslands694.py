class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y, path):
            if x < 0 or x >= m or y < 0 or y >= n or not grid[x][y]:
                return ""
            # marked as visited
            grid[x][y] = 0
            return path + dfs(x + 1, y, path + 'r') + '*' \
                        + dfs(x - 1, y, path + 'l') + '*' \
                        + dfs(x, y + 1, path + 'u') + '*' \
                        + dfs(x, y - 1, path + 'd') + '*'
        
        shape = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    shape.add(dfs(i, j, "*"))
        # print(shape)
        return len(shape)


class Solution2(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
                if not grid: return 0
        m = len(grid)
        n = len(grid[0])
         
        def dfs(i, j, direction):
            if i < 0 or j < 0 or i >= m or j >= n or not grid[i][j]:
                return
            l.append(direction)
            grid[i][j] = 0
            dfs(i, j+1 ,1)
            dfs(i, j-1 ,2)
            dfs(i-1, j, 3)
            dfs(i+1, j, 4)
            l.append(0)
        
        lset = set()
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    l = [] # reset l every time
                    dfs(i, j, 0)
                    if l:
                        lset.add(tuple(l))
        # print(lset)
        return len(lset)