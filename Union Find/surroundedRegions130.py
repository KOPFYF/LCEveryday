print(19%(-3))
print((-19)%3)

class Solution(object):
    def solve(self, grid):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not grid: return []
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dsu = DSU(m * n + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'O':
                    # if a 'O' node is on the boundry, connect it to the dummy node
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        dsu.union(i * n + j, m * n)  
                    # connect a 'O' node to its neighbour 'O' nodes
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 'O':
                            dsu.union(x * n + y, i * n + j)
        for i in range(m):
            for j in range(n):
                # if a 'O' node is not connected to the dummy node, it is captured
                if not dsu.isConnect(i * n + j, m * n):
                    grid[i][j] = 'X'
        
        
class DSU(object):
    # Union by size
    def __init__(self, n):
        self.parents = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parents[i] = i
    
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
            
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)