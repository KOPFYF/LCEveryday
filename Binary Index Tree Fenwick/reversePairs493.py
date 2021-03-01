'''
same as 315. Count of Smaller Numbers After Self
'''
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # compress index
        all_nums = list(set(nums + [x * 2 for x in nums]))
        rank = {val: i+1 for i, val in enumerate(sorted(all_nums))} # +1 for dummy node
        
        res, n = 0, len(nums)
        fw_tree = FenwickTree(len(rank))
        for i in range(n - 1, -1, -1): # backward
            res += fw_tree.query(rank[nums[i]] - 1)
            fw_tree.update(rank[nums[i] * 2], 1)
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