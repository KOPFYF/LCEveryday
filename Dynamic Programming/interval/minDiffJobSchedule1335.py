class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        # top down 1, right to left
        # i is the index of the last cut, k is the remaining cut
        n = len(job)
        if n < d: return -1
        
        @lru_cache(None)
        def dfs(i, k):
            # s[j:i] + dfs(j, k - 1)
            if k == 1:
                return max(job[:i])
            res, maxd = float('inf'), 0
            for j in range(i - 1, 0, -1):
                maxd = max(maxd, job[j])
                res = min(res, maxd + dfs(j, k - 1))
            return res
        
        return dfs(len(job), d)
        
        
        # top down 2, left to right
        # i is the index of the last cut, k is the remaining cut
        n = len(job)
        if n < d: return -1
        
        @lru_cache(None)
        def dfs(i, k):
            # s[:i] + s[i:j]
            if k == 1:
                return max(job[i:])
            res, maxd = float('inf'), 0
            # call dfs(j, k - 1) and eval job[i:j] j <= n - k
            for j in range(i, n - k + 1):
                maxd = max(maxd, job[j])
                res = min(res, maxd + dfs(j + 1, k - 1))
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

