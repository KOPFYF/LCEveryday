class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        res, mod = 0, 10**9 + 7
        fw_tree = FenwickTree(max(instructions))
        
        for i, num in enumerate(instructions):
            left = fw_tree.query(num - 1)
            right = i - fw_tree.query(num)
            res = (res + min(left, right)) % mod
            fw_tree.update(num, 1)
        
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
    



class Solution2:
    def createSortedArray(self, A: List[int]) -> int: 
        
        # TLE
        if not A or (n:=len(A)) <= 2: return 0
        nums = [A[0]]
        res = 0
        for a in A[1:]:
            i = bisect.bisect_left(nums, a)
            j = bisect.bisect_right(nums, a)
            res = res + min(i, len(nums) - j) 
            bisect.insort(nums, a)
        # print(nums)
        return res % (10**9 + 7)