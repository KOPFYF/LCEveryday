class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return nums[i]
            x, y = dfs(i + 1, j), dfs(i, j - 1)
            
            return max(nums[i] - x, nums[j] - y)
        
        return dfs(0, len(nums) - 1) >= 0