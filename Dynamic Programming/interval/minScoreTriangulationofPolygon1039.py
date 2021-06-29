class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        If we pick a side of our polygon, it can form n - 2 triangles. 
        Each such triangle forms 2 sub-polygons. 
        We can analyze n - 2 triangles, 
        and get the minimum score for sub-polygons using the recursion.
        """
        # top down DP
        memo = {}
        def dfs(i, j):
            if j - i < 2:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            # memo[(i, j)] = min([dfs(i, k) + dfs(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
            res = float('inf')
            for k in range(i + 1, j):
                res = min(dfs(i, k) + dfs(k, j) + A[i] * A[j] * A[k], res)
            memo[(i, j)] = res
            return memo[(i, j)]
        
        return dfs(0, len(A) - 1)