class Solution(object):
    def stoneGameV(self, stones):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        # DP bottom up O(n^2)
        # https://leetcode.com/problems/stone-game-v/discuss/807330/C++-O(N2)-DP
        n = len(stones)
        A = [0]
        for x in stones:
            A.append(A[-1] + x)
            
        dp = [[0] * (n+1) for _ in range(n+1)]
        f, g = [0] * (n+1), [0] * (n+1)
        x, y = [0] * (n+1), [0] * (n+1)
        
        for i in range(1,n+1):
            x[i], y[i] = i, i - 1
        
        for l in range(2, n + 1):
            for i in range(1, n+1):
                j = i + l - 1
                if j > n:
                    break

                half = (A[j] - A[i-1]) // 2
                
                while x[i] < j and A[x[i]] - A[i-1] <= half:
                    f[i] = max(f[i], A[x[i]] - A[i-1] + dp[i][x[i]])
                    x[i] += 1
                    
                while y[j] >= i and A[j] - A[y[j]] <= half:
                    g[j] = max(g[j], A[j] - A[y[j]] + dp[y[j]+1][j])
                    y[j] -= 1
                    
                dp[i][j] = max(f[i], g[j])

        return dp[1][n]


class Solution_TLE:
    def stoneGameV(self, A: List[int]) -> int:
        # DP, O(N^3) TLE
        n = len(A)
        prefix = [0] * (n + 1)
        for i, a in enumerate(A):
            prefix[i + 1] = prefix[i] + A[i]

        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j: 
                return 0
            res = 0
            for m in range(i, j):
                left = prefix[m + 1] - prefix[i]
                right = prefix[j + 1] - prefix[m + 1]
                if left <= right:
                    res = max(res, dfs(i, m) + left)
                if left >= right:
                    res = max(res, dfs(m + 1, j) + right)
                memo[(i, j)] = res    
            return res
        
        return dfs(0, n - 1)