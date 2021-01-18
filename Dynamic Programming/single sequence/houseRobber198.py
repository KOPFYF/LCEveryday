class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bottom up DP, time O(n), space O(n)
        # Base Cases
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for k in range(2, len(nums)):
            dp[k] = max(dp[k-2] + nums[k], dp[k-1])
        return dp[-1]


class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bottom up DP, time O(n), space O(1)
        if not nums: return 0
        dp2, dp1 = 0, 0
        
        for k in range(len(nums)):
            tmp = dp1
            dp1 = max(dp2 + nums[k], dp1)
            dp2 = tmp
        return dp1


class Solution3(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 3, top-down, DFS + memo
        # time: O(n), space: O(n)
        if not nums: return 0
        memo = {}
        def dfs(pos):
            if pos < 0:
                return 0
            if pos in memo:
                return memo[pos]
            memo[pos] = max(dfs(pos - 1), dfs(pos - 2) + nums[pos]);
            return memo[pos]
            
        return dfs(len(nums) - 1)

        