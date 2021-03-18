class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:   
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cnt = len(positions)
        dsu = DSU(m * n, cnt)
        
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in positions:
            index = x * n + y # flatten a 2d coordinate into a 1d value
            dsu.setParent(index)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and nx * n + ny in dsu.parents:
                    dsu.Union(index, nx * n + ny)
            res.append(dsu.count)
        return res
        
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