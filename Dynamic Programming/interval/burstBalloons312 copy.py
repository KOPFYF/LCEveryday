class Solution1(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i < k < j
        # dp[i][j] means the maximum coins we get after we burst all the balloons between i and j in the original array.
        # reverse thinking: assume that the balloon k we have chosen as the last to get burst
        # so it gets multiplied by the boundary elements of the array under consideration
        
        # top-down DP, time O(n^3) space O(n^2)
        A = [1] + nums + [1]
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        
        def dfs(i, j):
            if dp[i][j]: 
                return dp[i][j]
            if i > j:
                return 0

            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dfs(i, k) + A[i] * A[k] * A[j]  + dfs(k, j))

            return dp[i][j]

        return dfs(0, n - 1)


class Solution2(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bottom up DP, time O(n^3) space O(n^2)
        A = [1] + nums + [1]
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        
        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + A[i] * A[k] * A[j]  + dp[k][j])
        
        return dp[0][n-1]