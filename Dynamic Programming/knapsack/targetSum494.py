class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # top down, right to left
        @lru_cache(None)
        def dfs(pos, target):
            if pos < 0 and target == 0:
                return 1
            if pos < 0:
                return 0
            return dfs(pos - 1, target + nums[pos]) + dfs(pos - 1, target - nums[pos])
        
        return dfs(len(nums) - 1, S)

class Solution1:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # top down, left to right
        n = len(nums)
        
        @lru_cache(None)
        def dfs(pos, runsum):
            if runsum == target and pos == n:
                return 1
            elif pos == n:
                return 0
            
            return dfs(pos + 1, runsum + nums[pos]) + dfs(pos + 1, runsum - nums[pos])
        
        return dfs(0, 0)


class Solution2(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp={0:1}
        for i in range(len(nums)):
            newdp=collections.defaultdict(int)
            for key in dp:
                newdp[key+nums[i]]+=dp[key]
                newdp[key-nums[i]]+=dp[key]
            dp=newdp
        return dp[S] if S in dp else 0
            
            