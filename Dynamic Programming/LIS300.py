class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP, time O(n^2) space O(n)
        # DP[i] means the result ends at i
        # So for dp[i], dp[i] is max(dp[j] + 1), for all j < i and nums[j] < nums[i]
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range (1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        # [10,9,2,5,3,7,101,18]
        # [1, 1, 1, 2, 2, 3, 4, 4]
        return max(dp)