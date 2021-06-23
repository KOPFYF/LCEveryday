class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * n  for _ in range(n)]
        # 0 <= i < j < n
        for i in range(n - 1, -1, -1): 
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return n - dp[0][-1] <= k
                
        
        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1
        
        return dfs(0, len(s) - 1) <= k