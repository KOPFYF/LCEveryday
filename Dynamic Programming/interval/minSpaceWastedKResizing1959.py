'''
1 <= nums.length <= 200
1 <= nums[i] <= 10**6
0 <= k <= nums.length - 1

hint1: 
Given a range, how can you find the minimum waste if you can't perform any resize operations?

hint2:
Can we build our solution using dynamic programming using the current index and the number of resizing operations performed as the states?

'''

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        # dp(i, k) denote the minimum space wasted if we can resize k times of nums[i..n-1].
        # 区间型DP，找dp(j, k - 1)
        # time: O(n^2 k) and k < n <= 200
        # space: O(n k)
        n = len(nums)
        
        @lru_cache(None)
        def dfs(i, k):
            if i == n:
                return 0
            if k == 0:
                return max(nums[i:]) * len(nums[i:]) - sum(nums[i:])
            res = float('inf')
            curmax, runsum = nums[i], 0
            
            for j in range(i, n):
                curmax = max(curmax, nums[j])
                runsum += nums[j]
                wasted = curmax * (j - i + 1) - runsum
                res = min(res, dfs(j + 1, k - 1) + wasted)
            return res
        
        return dfs(0, k)
                
                
            
        