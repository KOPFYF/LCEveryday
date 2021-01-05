class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]: the number of distinct subsequences for s[0,i-1] and t[0,j-1];    
        @lru_cache(None)
        def dfs(i, j):
            if j == 0:
                return 1
            if i == 0:
                return 0

            if s[i - 1] == t[j - 1]:
                # given the match, t can choose or not choose
                res = dfs(i - 1, j - 1) + dfs(i - 1, j)
            else:
                res = dfs(i - 1, j)

            return res
        
        return dfs(len(s), len(t))