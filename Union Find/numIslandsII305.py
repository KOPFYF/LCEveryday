class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        dsu = DSU(m * n)
        grid = [[0] * n for _ in range(m)]
        def dfs(x, y):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    dsu.union(x * n + y, nx * n + ny)
            res.append(dsu.cnt) # append result for current position
        
        for x, y in positions:
            if grid[x][y] == 0:
                grid[x][y] = 1
                # for every new island, if union, it will --
                dsu.cnt += 1 # assume x, y is a new island
                dfs(x, y) # if x, y is connected, cnt-- so it does not hurt
            else: # it's set before so cnt does not change
                res.append(dsu.cnt)
        return res
            
        
class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.cnt = 0 # cnt++ when we meet a new island, cnt-- when we union
        
    def union(self, x, y):
        if not self.isconnected(x, y):
            px, py = self.find(x), self.find(y)
            self.parents[py] = px
            self.cnt -= 1
            
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def isconnected(self, x, y):
        return self.find(x) == self.find(y)


# Shorter
class Solution2:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            while x in pa:
                if pa[x] in pa:#path compress
                    pa[x] = pa[pa[x]]
                x = pa[x]
            return x    
        def union(x,y):
            pax,pay = find(x),find(y)
            if pax == pay:#union fail,has been unioned.
                return False
            pa[pax] = pay
            return True
        seen, pa, res, count = set(), {}, [], 0
        for x,y in positions:#connect with neighbor val==1,if union success,means one island disappear.
            if (x,y) not in seen:
                seen.add((x,y))
                count += 1
                for i,j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                    if (i,j) in seen and union((i,j), (x,y)):
                        count -= 1
            res.append(count)
        return res