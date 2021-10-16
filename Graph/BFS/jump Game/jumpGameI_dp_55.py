class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_ = 0
        for i in range(n):
            if i <= max_: # valid jump so far
                max_ = max(max_, i + nums[i])
        return max_ >= n - 1