class Solution:
    def minInsertions(self, s: str) -> int:
        # Top down DP, time O(n), space O(n)
        @lru_cache(None)
        def dfs(i, j):
            if i >= j: return 0
            # if i == j + 1: return s[i] == s[j]
            return dfs(i + 1, j - 1) if s[i] == s[j] else min(dfs(i, j - 1), dfs(i + 1, j)) + 1
        
        return dfs(0, len(s) - 1)
    
        # Bottom up DP, time O(n^2), space O(n^2)
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j - 1, -1, -1):
                dp[i][j] = dp[i + 1][j - 1] if s[i] == s[j] else min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]