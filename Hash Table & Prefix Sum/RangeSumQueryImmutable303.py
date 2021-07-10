class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        self.presum = [0] * (self.size + 1)
        for i in range(1, self.size + 1):
            self.presum[i] = self.presum[i - 1] + nums[i - 1] 

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right + 1] - self.presum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)