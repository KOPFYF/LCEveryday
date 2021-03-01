'''
Thoughts:
    1. backward
    2. insert/simulate
    
Example:
    1, 2, 5, 6
    1, 2, 3, 4
    
fw: 1, 0, 0, 1
    1, 2, 3, 4
    get presum of count/freq

Approaches
    1. insert/insort O(n)
    2. skip-list O(logn)
    3. Fenwick tree
'''

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # compress index
        all_nums = list(set(nums))
        rank = {val: i+1 for i, val in enumerate(all_nums)} # +1 for dummy node
        
        n = len(nums)
        res = [0] * n
        fw_tree = FenwickTree(n)
        for i in range(n - 1, -1, -1): # backward
            res[i] = fw_tree.query(rank[nums[i]] - 1)
            fw_tree.update(rank[nums[i]], 1)
        return res
        
        
        
class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)


    def update(self,i, delta):
        # go down
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)


    def query(self, i):
        # go up/go to parent
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)
        return s


    def _lowbit(self, x):
        # return x & (~x + 1)
        return x & -x      