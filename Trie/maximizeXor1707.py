class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        trie, n = Trie(), len(queries)
        queries_sort = sorted(enumerate(queries), key=lambda x: x[1][1]) # sorted by m
        
        res, j = [-1] * n, 0
        for i, (x, m) in queries_sort:
            while j < len(nums) and nums[j] < m:
                trie.insert(nums[j])
                j += 1
            res[i] = trie.query(x)
        return res
        
    
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1 # get i-th bit
            if bit not in node:
                node[bit] = {}
            node = node[bit]
    
    def query(self, num):
        # O(32)
        if not self.root: # no node
            return -1
        node, res = self.root, 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1 # get i-th bit
            if 1 - bit in node: # greedy, chose complement
                # find a 1/0, go to node.zero/node.one
                node = node[1 - bit]
                res |= (1 << i)
            else: # only one path, follow it
                node = node[bit]
        return res
            

class Solution2:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # soln 2
        nums.sort()
        queries_sort = sorted(enumerate(queries), key=lambda x: x[1][1])
        res = [-1] * len(queries)
        
        for k in range(31, -1, -1):
            prefixes = set()
            j = 0
            for i, (x, m) in queries_sort:
                while j < len(nums) and nums[j] <= m:
                    prefixes.add(nums[j] >> k)
                    j += 1
                if prefixes:
                    res[i] <<= 1
                    nxt = res[i] + 1
                    if (x >> k) ^ nxt in prefixes:
                        res[i] = nxt
        return res
            
            