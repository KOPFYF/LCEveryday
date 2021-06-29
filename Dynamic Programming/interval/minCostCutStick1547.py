class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # top down
        cuts.sort()
        cuts = [0] + cuts + [n]
        @lru_cache(None)
        def dfs(i, j):
            if j - i == 1:
                return 0
            res = float('inf')
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + cuts[j] - cuts[i])
            return res
        
        return dfs(0, len(cuts) - 1)

        # Bottom up
        cuts.sort()
        cuts = [0] + cuts + [n]
        k = len(cuts)
        
        dp = [[0] * k for _ in range(k)]
        for i in range(k-1, -1, -1):
            for j in range(i+2, k):
                dp[i][j] = cuts[j] - cuts[i] + \
                           min(dp[i][k] + dp[k][j] for k in range(i+1, j))
        
        return dp[0][-1]