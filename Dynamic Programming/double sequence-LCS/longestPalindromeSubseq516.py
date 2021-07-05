class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for d in range(1, n + 1):
            for i in range(n - d):
                j = i + d
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
                
            
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            res = float('-inf')
            if s[i] == s[j]:
                return 2 + dfs(i + 1, j - 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))
            
        return dfs(0, len(s) - 1)