class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # greedy + sort
        nums.sort()
        s, cur = sum(nums), 0
        res = []
        for i in range(len(nums) - 1, -1, -1):
            if cur > s - cur:
                break
            cur += nums[i]
            res.append(nums[i])
        return res