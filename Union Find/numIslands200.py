class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cnt = sum(grid[i][j]=='1' for i in range(m) for j in range(n))
        dsu = DSU(m * n, cnt)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            dsu.union(x * n + y, i * n + j)
        return dsu.count
                            
                            
      
class DSU(object):
    # Union by size
    def __init__(self, n, cnt):
        self.parents = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parents[i] = i
        self.count = cnt # add a count here!
        
    
    def find(self, x):
        # Path compression
        if self.parents[x] != x: # if x is nott root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        if self.size[rootx] <= self.size[rooty]:
            self.parents[rootx] = rooty
            self.size[rooty] += self.size[rootx]
        else:
            self.parents[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        # if union success, cnt -= 1
        self.count -= 1