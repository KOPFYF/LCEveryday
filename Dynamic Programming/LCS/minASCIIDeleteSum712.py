class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # Bottom UP 2D DP, time O(n1*n2), space O(n1*n2)
        n1, n2 = len(s1), len(s2)
        l1, l2 = [ord(c) for c in s1], [ord(c) for c in s2]
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + l1[i - 1]
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + l2[j - 1]
            
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if l1[i - 1] == l2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + l1[i - 1], dp[i][j - 1] + l2[j - 1])
        return dp[-1][-1]


class Solution2:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # Top Down 2D DP, time O(n1*n2), space O(n1*n2)
        l1, l2 = [ord(c) for c in s1], [ord(c) for c in s2]
        
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 and j == 0: return 0
            if i == 0: return dfs(i, j - 1) + l2[j - 1]
            if j == 0: return dfs(i - 1, j) + l1[i - 1]
            
            if l1[i - 1] == l2[j - 1]: 
                return dfs(i - 1, j - 1)
            else:
                return min(dfs(i - 1, j) + l1[i - 1], dfs(i, j - 1) + l2[j - 1])
        
        return dfs(len(s1), len(s2))