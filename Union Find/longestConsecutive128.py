class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dsu = DSU(n)
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                continue # skip dup
            hashmap[num] = i
            if num - 1 in hashmap:
                dsu.union(i, hashmap[num - 1])
            if num + 1 in hashmap:
                dsu.union(i, hashmap[num + 1])
        return dsu.findmax()
        
              
class DSU(object):
    # Union by size/rank
    def __init__(self, n):
        self.parents = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parents[i] = i
    
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
            
    def findmax(self):
        return max(self.size)
            