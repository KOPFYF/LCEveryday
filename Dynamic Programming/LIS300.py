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

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top down DP
        n = len(nums)
        @lru_cache(None)
        def dfs(i):
            if i == 0: return 1
            res = 1 # base case it's the element itself if no nums[j] < nums[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(dfs(j) + 1, res) 
            return res
        
        return max(dfs(i) for i in range(n))