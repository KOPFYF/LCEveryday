class Solutiom:
    def minDistance(self, word1: str, word2: str) -> int:
        # ttop down
        m , n = len(word1), len(word2)
        @lru_cache(None)
        def dfs(i, j):
            if i == m or j == n:
                return n - j + m - i
            
            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            else:
                res = min(dfs(i+1, j+1), dfs(i, j+1), dfs(i+1, j)) + 1
            return res
        
        return dfs(0, 0)

        # Bottom up 2D DP, time O(m * n), space O(m * n)
        m, n = len(word1), len(word2)       
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i][j - 1]: delete, dp[i - 1][j]: insert, dp[i - 1][j - 1]: replace
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        
        return dp[-1][-1]




class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    ans = dfs(i + 1, j + 1)
                else: 
                    insert = 1 + dfs(i, j + 1)
                    delete = 1 + dfs(i + 1, j)
                    replace = 1 + dfs(i + 1, j + 1)
                    ans = min(insert, delete, replace)
                memo[(i, j)] = ans
            return memo[(i, j)]
        
        return dfs(0, 0)

        