class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # Top down, TLE
        @lru_cache(None)
        def dfs(i, j, cnt):
            if i <= 0 or j <= 0: 
                return cnt
            cnt1 = cnt
            if A[i - 1] == B[j - 1]:
                cnt1 = dfs(i - 1, j - 1, cnt + 1)
            cnt2, cnt3 = dfs(i, j - 1, 0), dfs(i - 1, j, 0) # reset cnt to 0 if not match
            return max(cnt1, cnt2, cnt3)

        return dfs(len(A), len(B), 0)
        
        
        # LCS DP
        # dp[i][j] means the length of longest common subarray ending with nums[i] and nums[j]
        m, n = len(A), len(B)
        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(dp[i][j], res)
                # else:
                #     dp[i][j] = 0 # reset if not match
        return res
    
    