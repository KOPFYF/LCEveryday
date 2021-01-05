class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(None)
        def dfs(d, f, target):
            if target < 0:
                return 0
            if d == 0:
                return 0 if target > 0 else 1
            res = 0
            for num in range(1, f + 1):
                res += dfs(d - 1, f, target - num)
            return res
        
        return dfs(d, f, target) % (10**9 + 7)