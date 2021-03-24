class DSU:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parents[px] = py


class DSU1(object):
    # just path compression
    def __init__(self, n):
        self.parents = list(range(n))
    
    def find(self, x):
        if self.parents[x] != x: # if x is not root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class DSU2(object):
    # path compression + union by size
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parents[x] != x: # if x is not root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px # px's size is always bigger
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.size[py] = self.size[px]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class DSU3(object):
    # path compression + union by rank
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parents[x] != x: # if x is not root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parents[px] = py
            elif self.rank[py] < self.rank[px]:
                self.parents[py] = px
            else:
                self.parents[px] = py
                self.rank[py] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

