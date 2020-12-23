class Solution(object):
    def numIslands2(self, m, n, positions):
        disJointSet = DisJointSet()
        disJointSet.forest = [1] * (m * n)
        res = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in positions:
            index = x * n + y # flatten a 2d coordinate into a 1d value
            disJointSet.setParent(index)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and nx * n + ny in disJointSet.parents:
                    disJointSet.Union(index, nx * n + ny)
            res.append(disJointSet.count)
        return res
                    
class DisJointSet(object):
    
    def __init__(self):
        self.parents = {} # dict to store parent for each node
        self.count = 0
        self.forest = [] # size of set
        
    def Union(self, x, y):
        set1 = self.find(x) # find root of x
        set2 = self.find(y) # find root of y
        if set1 != set2:      
            # set parent to the bigger id
            if self.forest[set1] < self.forest[set2]:
                    self.parents[set1] = set2
                    self.forest[set2] += self.forest[set1]
            else:
                self.parents[set2] = set1
                self.forest[set1] += self.forest[set2]
            self.count -= 1 # union and reduce the # of sets
    
    def find(self, i):
        # return the oldest parent as set id
        while self.parents[i] != i:
            i = self.parents[i]
        return i
    
    def setParent(self, x):
        if self.parents.get(x): # if set before, skip
            return
        self.parents[x] = x
        self.count += 1

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