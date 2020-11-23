class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Binary Seach + Prefix Sum, time O(nlogn), space O(1)
        def check(nums, target, n):
            # return boolean, if we can split into <=n parts with max(sum) <= target
            curSum, cnt = 0, 1
            for num in nums:
                curSum += num
                if curSum > target:
                    curSum = num
                    cnt += 1
                    if cnt > n:
                        return False
            return True
        
        l, r = max(nums), sum(nums)
        if m == 1:
            return r
        while l < r:
            mid = l + (r - l) // 2
            if check(nums, mid, m):
                # we can split into m with mid, should decrease mid
                r = mid
            else:
                l = mid + 1
        return l



class SolutionTLE:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Top down DP + Prefix Sum, Time O(mn^2), Space O(n) 
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n): 
            prefix[i + 1] = prefix[i] + nums[i]

        @lru_cache(None)
        def dfs(i, m): 
            """Return the minimum of largest sum among m subarrays of nums[i:]."""
            if m == 1: 
                return prefix[-1] - prefix[i]
            res = float('inf') #if not enough elements for m subarrays, inf is returned 
            for j in range(i + 1, len(nums)): 
                left = prefix[j] - prefix[i]
                right = dfs(j, m - 1)
                res = min(res, max(left, right))
            return res
        
        return dfs(0, m)