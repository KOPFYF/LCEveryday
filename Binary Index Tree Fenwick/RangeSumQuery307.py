class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.fw_tree = FenwickTree(len(nums))
        for i, num in enumerate(nums):
            self.fw_tree.update(i + 1, num)

    def update(self, index: int, val: int) -> None:
        self.fw_tree.update(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        # presum = [0, 3, 5, 6] => presum[3] - presum[1]
        return self.fw_tree.query(right + 1) - self.fw_tree.query(left)
        
        
        
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
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)