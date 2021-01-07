class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dfs + memo
        @lru_cache(None)
        def dfs(i, j):
            if i >= j: return 0
            if i >= j - 2: 
                # this base case could be commented
                # window size is like [8, 9] or [8, 10]
                # [8, 9] we guess 8, [8, 10] we guess 9!
                return j - 1
            res = float('inf')
            for k in range(i, j + 1):
                tmp = k + max(dfs(i, k - 1), dfs(k + 1, j))
                res = min(res, tmp)
            return res
        
        return dfs(1, n)


class Solution2:
    def getMoneyAmount(self, n: int) -> int:
        # bottom up
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for j in range(2, n + 1): # 0 < i < j <= n
            for i in range(j - 1, 0, -1):
                min_ = float('inf')
                for k in range(i + 1, j):
                    tmp = k + max(dp[i][k - 1], dp[k + 1][j])
                    min_ = min(min_, tmp)
                if i + 1 == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = min_
        return dp[1][n]