class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 2D Bottom Up DP, time O(n1*n2), space O(n1*n2)
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if s1 == "": return s2 == s3
        if s2 == "": return s1 == s3
        if n1 + n2 != n3: return False
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = 1
        
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (s1[i - 1] == s3[i - 1 + j] and dp[i - 1][j]) \
                        or (s2[j - 1] == s3[i - 1 + j] and dp[i][j - 1])
        
        return dp[-1][-1]


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 2D Top Down DP, time O(n1*n2), space O(n1*n2)
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if s1 == "": return s2 == s3
        if s2 == "": return s1 == s3
        if n1 + n2 != n3: return False
        
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 and j == 0:
                return True
            if i == 0 and s2[j - 1] == s3[j - 1]:
                return dfs(i, j - 1)
            if j == 0 and s1[i - 1] == s3[i - 1]:
                return dfs(i - 1, j)
            
            tmp1, tmp2 = False, False
            if i > 0 and s1[i - 1] == s3[i - 1 + j]:
                tmp1 = dfs(i - 1, j)
            if j > 0 and s2[j - 1] == s3[i - 1 + j]:
                tmp2 = dfs(i, j - 1)
            return tmp1 or tmp2
        
        return dfs(n1, n2)


