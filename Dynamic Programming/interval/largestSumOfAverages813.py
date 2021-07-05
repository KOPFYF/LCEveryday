class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        @lru_cache(None)
        def dfs(i, k):
            # s[:i] with k subarrays
            if i < k: # no way to split
                return 0
            if k == 1:
                return sum(nums[:i]) / i
            cur, res = 0, 0
            # call dfs(j, k - 1) and check nums[j:i]
            for j in range(i - 1, 0, -1):
                cur += nums[j]
                res = max(res, dfs(j, k - 1) + cur / (i - j))
            return res
        
        return dfs(len(nums), k)