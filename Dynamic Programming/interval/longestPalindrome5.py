class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, - 1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and (j - i + 1) > len(res):
                    res = s[i:j+1]
        return res
        
        # TLE
        n = len(s)
        res = ""
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return False
            if i == j:
                return True
            if i == j - 1:
                return s[i] == s[j]
            return s[i] == s[j] and dfs(i + 1, j - 1)
            
        for i in range(n - 1, - 1, -1):
            for j in range(i, n):
                if dfs(i, j) and (j - i + 1) > len(res):
                    res = s[i:j+1]
        return res
                    
            