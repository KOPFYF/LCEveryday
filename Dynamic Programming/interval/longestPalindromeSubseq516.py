class Solution_td:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + dfs(i + 1, j - 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))
            
        return dfs(0, len(s) - 1)



class Solution_bu(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Bottom Up 2D dp
        n = len(s)
        if s == s[::-1]: return n
        dp = [[0] * n  for i in range(n)]

        # 0 <= i < j < n
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
    
        # Compress it to 1D DP, https://tinyurl.com/y2jj4z2o
        # 把二维 dp 数组压缩成一维，一般来说是把第一个维度，也就是 i 这个维度去掉，只剩下 j 这个维度。
        # 压缩后的一维 dp 数组就是之前二维 dp 数组的 dp[i][..] 那一行
        n = len(s)
        if s == s[::-1]: return n
        dp = [0] * n 

        # 0 <= i < j < n
        # 循环遍历 i 和 j 的顺序为从左向右，从下向上
        # 那么如果我们想得到 dp[i+1][j-1]，就必须在它被覆盖之前用一个临时变量 temp 把它存起来
        # 并把这个变量的值保留到计算 dp[i][j] 的时候
        for i in range(n - 1, -1, -1):
            # dp[i][i] = 1
            dp[i] = 1
            pre = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    # dp[i][j] = dp[i + 1][j - 1] + 2
                    dp[j] = pre + 2
                else:
                    # dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    dp[j] = max(dp[j], dp[j - 1])
                pre = temp
        return dp[n - 1]
        



        
    

        