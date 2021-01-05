class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
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