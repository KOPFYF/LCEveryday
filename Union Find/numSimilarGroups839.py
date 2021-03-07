class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self._similar(strs[i], strs[j]):
                    dsu.union(i, j)
        
        # print(dsu.parents, [dsu.find(i) for i in range(n)])
        return len(set(dsu.find(i) for i in range(n)))
    
    def _similar(self, a, b):
        s = 0
        for k in range(len(a)):
            if a[k] != b[k]:
                s += 1
                if s > 2:
                    return False
        return s in (0, 2) # words could be dup
            
              
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