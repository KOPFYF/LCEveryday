class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # Top down, O((M+N)^2)/O((M+N)^2)
        s = word1 + word2
        m, n, self.res = len(word1), len(word2), 0
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j: return 0
            if i == j: return 1
            
            if s[i] == s[j]:
                tmp = dfs(i+1, j-1) + 2
                if i < m and j >= m: 
                        self.res = max(self.res, tmp)
                return tmp
            else:
                return max(dfs(i, j-1), dfs(i+1, j))
        dfs(0, m + n - 1)
        return self.res

        # DP bottom up, O((M+N)^2)
        s = word1 + word2
        m, n, res = len(word1), len(word2), 0
        
        dp = [[0] * (m + n) for _ in range(m + n)]
        for j in range(m + n):
            dp[j][j] = 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 2 if i + 1 == j else dp[i+1][j-1] + 2
                    # if the palindrome includes both string consider it as a valid
                    if i < m and j >= m: 
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return res

        
    
        # Top down, O((M+N)^2)/O((M+N)^2)
        s = word1 + word2
        m, n, res = len(word1), len(word2), 0
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]:
                return dfs(i+1, j-1) + 2
            else:
                return max(dfs(i, j-1), dfs(i+1, j))
            
        for ch in ascii_lowercase:
            i = word1.find(ch)
            j = word2.rfind(ch)
            if i != -1 and j != -1:
                res = max(res, dfs(i, j + m))
        return res
            
        
        
    
    
