class Solution_uf:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # for a connected graph, the number of stones we can remove is len(graph)-1
        # What is the number of islands?
        dsu = DSU(20001)
        
        # ~x = - x - 1
        # to represent both row and columns in the same dimension
        # Search on the index, not the points
        # The number of islands of points,
        # is the same as the number of islands of indexes.
        for x, y in stones:
            # dsu.union(x, y + 10000)
            dsu.union(x, ~y)
            
        return len(stones) - len(set(dsu.find(x) for x, y in stones))
               
        
class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if not self.isConnect(x, y):
            self.parents[self.find(x)] = self.find(y)
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)


class Solution_dfs:
    # define an island as number of points that are connected by row or column
    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)
        
        points, island, rows, cols = {(i, j) for i, j in stones}, 0, collections.defaultdict(list), collections.defaultdict(list)
        
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island