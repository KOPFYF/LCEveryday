class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(s1, s2):
            n, n2 = len(s1), len(s2)
            if n != n2:
                return False
            idx = []
            for i in range(n):
                if s1[i] != s2[i]:
                    idx.append(i)
                    if len(idx) > 2:
                        return False
            # print(s1, s2, idx)
            if len(idx) == 0:
                return True
            elif len(idx) == 1:
                return False
            elif len(idx) == 2:
                i, j = idx
                return s1[i] == s2[j] and s1[j] == s2[i]
        
        l = len(strs)
        dsu = DSU(l)
        for i in range(l):
            for j in range(i + 1, l):
                s1, s2 = strs[i], strs[j]
                if check(s1, s2):
                    dsu.union(i, j)
        
        groups = set()
        for i in range(l):
            p_idx = dsu.find(i)
            groups.add(p_idx)
        return len(groups)
                    
                    
                    
class DSU:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parents[px] = py


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