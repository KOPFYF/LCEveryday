class Solution_bug:
    def minimumMoves(self, s: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            res = 1 + dfs(i + 1, j)
            # if s[j] == s[j - 1]:
            #     res = min(res, dfs(i, j - 2) + 1)
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    # max(1, +) is vital here because  if + is 0
                    # failed on this case: [16,13,13,10,12]
                    res = min(res, max(1, dfs(i + 1, k - 1) + dfs(k + 1, j)))
            return res
        
        return dfs(0, len(s) - 1)


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        memo = {}
        return self.dfs(arr, 0, len(arr) - 1, memo)

    def dfs(self, arr, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        res = 1 + self.dfs(arr, i + 1, j, memo)

        for k in range(i + 1, j + 1):
            if arr[i] == arr[k]:
                res = min(res, max(1, self.dfs(arr, i + 1, k - 1, memo)) + \
                          self.dfs(arr, k + 1, j, memo))
        memo[(i, j)] = res
        return memo[(i, j)]


class Solution_top_down:
    def minimumMoves(self, A: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            res = dp(i, j - 1) + 1
            if A[j] == A[j - 1]:
                res = min(res, dp(i, j - 2) + 1)
            for k in range(i, j - 1):
                if A[j] == A[k]:
                    res = min(res, dp(i, k - 1) + dp(k + 1, j - 1))
            return res
        return dp(0, len(A) - 1)


class Solution_bottom_up(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [[0] * len(arr) for _ in range(len(arr))]
        for j in range(len(arr)):
            for i in range(j, -1, -1):
                r = len(arr)
                if arr[i] == arr[j]:
                    r = 1 if i + 1 > j - 1 or dp[i+1][j-1] == 0 else dp[i+1][j-1]
                for k in range(i, j):
                    r = min(r, dp[i][k] + dp[k+1][j])
                dp[i][j] = r
        return dp[0][len(arr)-1]