class UnionFind: 
    def __init__(self, n): 
        self.parent = list(range(n))
        self.span = [[n, 0] for _ in range(n)]
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q, n): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: 
            return False # already connected 
        self.parent[prt] = qrt
        pp = p % n # get row
        qq = q % n
        self.span[qrt][0] = min(self.span[qrt][0], self.span[prt][0], pp, qq)
        self.span[qrt][1] = max(self.span[qrt][1], self.span[prt][1], pp, qq)
        return True 
    

class Solution:
    def latestDayToCross(self, m: int, n: int, cells: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]
        
        uf = UnionFind(m * n)
        for step, (i, j) in enumerate(cells): 
            i, j = i - 1, j - 1
            grid[i][j] = 1
            cell = i * n + j
            for ii, jj in (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1): 
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]: 
                    new_cell = ii * n + jj 
                    uf.union(cell, new_cell, n)
                    if uf.span[uf.find(cell)] == [0, n-1]: 
                        return step 