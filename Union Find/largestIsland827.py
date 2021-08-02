class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for ii, jj in ((i-1, j), (i, j-1)):
                        if 0 <= ii < n and 0 <= jj < n and grid[ii][jj]:
                            dsu.union(i*n + j, ii*n + jj)
        freq = defaultdict(int)
        for i in range(n * n):
            freq[dsu.find(i)] += 1
        
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, freq[dsu.parent[i*n + j]])
                else:
                    cand, seen = 1, set() # 0 cand can connect 4 dirs at most
                    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj]:
                            p = dsu.parent[ni*n + nj]
                            if p not in seen:
                                seen.add(p)
                                cand += freq[p]
                    res = max(res, cand)
        return res
                            
                            
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.size[px] > self.size[py]:
            px, py = py, px # size: py > px
        self.parent[px] = py
        self.size[px] += self.size[py]
        self.size[py] = self.size[px]
        return True
        