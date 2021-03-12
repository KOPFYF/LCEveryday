class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # union find O(n)/O(n)
        dsu = DSU(26)
        for equ in equations:
            if equ[1] == "=":
                dsu.union(ord(equ[0]) - ord('a'), ord(equ[-1]) - ord('a'))
        
        for equ in equations:
            if equ[1] == "!":
                if dsu.find(ord(equ[0]) - ord('a')) == dsu.find(ord(equ[-1]) - ord('a')):
                    return False
        return True
        
        
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