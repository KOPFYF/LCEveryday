class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if n <= 1:
            return 0
        i, res = 0, float('inf')
        while i + k - 1 < n:
            res = min(res, nums[i+k-1] - nums[i])
            i += 1
        return res