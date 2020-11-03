class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # top down DP
        memo = {}
        def dfs(i, j):
            if j - i < 2:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            # memo[(i, j)] = min([dfs(i, k) + dfs(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
            min_ = float('inf')
            for k in range(i + 1, j):
                min_ = min(dfs(i, k) + dfs(k, j) + A[i] * A[j] * A[k], min_)
            memo[(i, j)] = min_
            return memo[(i, j)]
        
        return dfs(0, len(A) - 1)