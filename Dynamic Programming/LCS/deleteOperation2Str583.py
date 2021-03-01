class Solution:
    def minDistance(self, word1: str, word2: str) -> int:  
        # soln 1
        m, n = len(word1), len(word2)
        @lru_cache(None)
        def dfs(i, j):
            if i == m and j == n:
                return 0
            if i == m or j == n:
                return n - j or m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j + 1)) + 1
    
        return dfs(0, 0)

        # soln 2
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 and j == 0:
                return 0
            if i == 0 or j == 0:
                return j or i
            
            return dfs(i - 1, j - 1) if word1[i - 1] == word2[j - 1] \
                    else min(dfs(i, j - 1), dfs(i - 1, j)) + 1
        
        return dfs(len(word1), len(word2))

        # bottom up
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], \
                                   dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2 * dp[m][n]