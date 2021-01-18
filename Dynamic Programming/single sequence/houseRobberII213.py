class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # prev, curr = curr, max(curr, prev+nums[i])
        # Bottom up DP, base on house robber 1, just rob max(nums[1:], nums[:-1])
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        def dp(nums):
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]
        return max(dp(nums[1:]), dp(nums[:-1]))