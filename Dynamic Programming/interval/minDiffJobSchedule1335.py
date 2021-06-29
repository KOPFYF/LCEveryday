class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        # top down
        # i is the index of the last cut, j is the remaining days
        n = len(job)
        if n < d: return -1
        
        @lru_cache(None)
        def dfs(i, j):
            if j == 1:
                return max(job[i:])
            res, maxd = float('inf'), 0
            for k in range(i, n - j + 1):
                maxd = max(maxd, job[k])
                res = min(res, maxd + dfs(k + 1, j - 1))
            return res
        
        return dfs(0, d)

        # Bottom up, O(nnd)/O(nd)
        # i from 0 to n - 1, j from 0 to d - 1
        
        n = len(job)
        if n < d: return -1
        dp = [[0] * n for i in range(d)]
        dp[0][0] = job[0] # all jobs need to be in one day
        for i in range(1, n):
            # the base case, all jobs need to be finish in one day
            dp[0][i] = max(job[i], dp[0][i-1])
        
        for j in range(1, d): # given j days, i should be at least j 
            for i in range(j, n): # j <= i < n
                localMax = job[i]
                dp[j][i] = float('inf');
                for k in range(i, j - 1, -1): # search range k = [j, i]
                    localMax = max(localMax, job[k])
                    # 2 choices, keep up current diff, or switch to next day
                    dp[j][i] = min(dp[j][i], dp[j - 1][k - 1] + localMax)
        
        return dp[-1][-1]

