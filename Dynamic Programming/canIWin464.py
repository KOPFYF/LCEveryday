class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # DFS + memo, time O(n^2) 492 ms, space O(n), 34.9 MB
        if maxChoosableInteger * (1 + maxChoosableInteger) / 2 < desiredTotal:
            return False
        memo = {}
        
        def dfs(nums, total):
            # base case, after we pick the max, we will win
            if nums[-1] >= total:
                return True
            
            nums_k = tuple(nums) # hash with tuple, faster than str()
            if nums_k in memo:
                return memo[nums_k]
            
            # next player loop all choices after we pick nums[i]
            for i in range(len(nums)):
                if not dfs(nums[:i] + nums[i+1:], total - nums[i]):
                    # next player loses with nums[i] picked, we win
                    memo[nums_k] = True
                    return True
            # next player wins all choices, we lose
            memo[nums_k] = False
            return False
        
        return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal)