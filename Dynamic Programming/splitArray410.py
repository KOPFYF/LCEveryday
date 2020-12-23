class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:      
        # Top down DP + Prefix Sum, Time O(mn^2), Space O(n) 
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n): 
            prefix[i + 1] = prefix[i] + nums[i]

        @lru_cache(None)
        def dfs(i, m): 
            if i == n:
                return 0
            if m == 1: 
                return prefix[-1] - prefix[i]
            res = float('inf') #if not enough elements for m subarrays, inf is returned 
            for j in range(i + 1, len(nums)): 
                left = prefix[j] - prefix[i]
                right = dfs(j, m - 1)
                res = min(res, max(left, right))
                if left > right: # this judgement speed it up !!! without it TLE
                    break
            return res
        
        return dfs(0, m)