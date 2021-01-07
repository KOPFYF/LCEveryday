class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        @lru_cache(None)
        def dfs(pos, target):
            if pos < 0 and target == 0:
                return 1
            if pos < 0:
                return 0
            return dfs(pos - 1, target + nums[pos]) + dfs(pos - 1, target - nums[pos])
        
        return dfs(len(nums) - 1, S)
            
            