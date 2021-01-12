class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # step 1: union all swaps
        n = len(target)
        uf = DSU(n)
        for u, v in allowedSwaps:
            uf.union(u, v)
        
        # Step 2: create group of lists based on union results
        d1, d2 = defaultdict(list), defaultdict(list)
        for i in range(n):
            d1[uf.find(i)].append(source[i]) 
            d2[uf.find(i)].append(target[i]) 
        
        # Step 3: define a count function to count overlapped items for single group
        def common_count(l1, l2):
            cnt = 0
            c1, c2 = Counter(l1), Counter(l2)
            for k1 in c1:
                if k1 in c2:
                    cnt += min(c1[k1], c2[k1])
            return cnt
        
        # Step 4: loop dict and accumulate overlapped items for all groups
        res = 0
        for k in d1.keys():
            l1, l2 = d1[k], d2[k]
            res += common_count(l1, l2)
            
        # Step 5: return unmatched items
        return n - res
        
# Union Find Class        
class DSU(object):
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x: # if x is not root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)