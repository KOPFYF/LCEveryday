'''
If you take a number, you might as well take them all. Keep track of what the value is of the subset of the input with maximum M when you either take or don't take M.

nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)
points: [0, 0, 4, 9, 4] <- This is the gold in each house!

The condition that we cannot pick adjacent values is similar to the House Robber question that we cannot rob adjacent houses. Simply pass points into the rob function for a quick win 🌝!
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # reduce to house robber
        points = [0] * (max(nums) + 1)
        for num in nums:
            points[num] += num
        # print(points)
        return self.rob(points)
    
    def rob(self, nums):
        @lru_cache(None)
        def dfs(pos):
            if pos < 0:
                return 0
            return max(dfs(pos - 1), dfs(pos - 2) + nums[pos])
        
        return dfs(len(nums) - 1)
    
    def rob2(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for k in range(2, len(nums)):
            dp[k] = max(dp[k-2] + nums[k], dp[k-1])
        return dp[-1]