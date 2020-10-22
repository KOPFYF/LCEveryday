class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 0/1 knapack
        # the differences between this problem and 518. Coin Change 2. In this problem, we CANNOT reuse an element while it can be reused in LT518. That is why we have dp[i-1][j-nums[i-1]] in this problem and dp[i][j-coins[i-1]] in LT518
        # from left to right means dp[i][j] = dp[i][j-nums[i-1]])
        # from right to left means dp[i][j] = dp[i-1][j-nums[i-1]]
        # The reason is that, from 2D DP we can see DP[i][j] = DP[i-1][j] or DP[i-1][j-num], DP[i][j] relies on previous DP values DP[i-1][j] and DP[i-1][j-num].
        # If we don't go from high to low however go from low to high, we would end up have DP[i][j] = DP[i-1][j] or DP[i][j-num] where DP[i][j-num] (or equally dp[j-num]) will be refreshed at previous steps in current iteration.

        s = sum(nums)
        if s % 2:
            return False
        else:
            target = s / 2
        
        dp = [0] * (target + 1) # can we get a subgroup with sum = target
        dp[0] = 1
        for num in nums:
            for j in range(target, 0, -1):
                if j - num >= 0:
                    # reverse is necessary 
                    dp[j] = dp[j] or dp[j - num]
        return dp[target]
    
        
