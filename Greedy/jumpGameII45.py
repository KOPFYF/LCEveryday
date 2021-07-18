class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # you can always reach the last index
        # the minimum number of jumps
        
        # O(n) greedy
        n = len(nums)
        jumps, curend, curmax = 0, 0, 0
        for i in range(n - 1):
            curmax = max(curmax, i + nums[i]) # greedy
            if i == curend:
                jumps += 1
                curend = curmax # exhausted
        return jumps
        
        # Same as 763. Partition Labels
        if len(nums) <= 1: return 0
        res = 1
        l, r = 0, nums[0] # initial reachable range
        
        while r < len(nums) - 1:
            res += 1
            nxt = max(i + nums[i] for i in range(l, r+1))
            l, r = r, nxt
        
        return res
        
        # O(n^2) DP, TLE, 1 <= nums.length <= 104
        n = len(nums)
        dp = [float('inf')] * n # at index i, dp[i] means the min jump
        dp[0] = 0
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
        