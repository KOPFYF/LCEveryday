class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # min number of swaps = N - number of connected components
        n = len(row) // 2
        dsu = DSU(n)
        for i in range(n):
            # pick 2 neighbor people
            person1, person2 = row[2 * i], row[2 * i + 1]
            # union if each person is from different couples
            # if u, v are couples already, u//2 = v//2 (couple id)
            couple1, couple2 = person1 // 2, person2 // 2
            dsu.union(couple1, couple2)
        return n - dsu.cnt
          
        
class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        self.cnt = n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if not self.isConnect(x, y):
            self.parents[self.find(x)] = self.find(y)
            self.cnt -= 1
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)