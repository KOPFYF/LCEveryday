class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        
        def dfs(pos, path):
            if len(path) > 1:
                res.add(tuple(path[:]))
            
            for i in range(pos, n):
                if not path or nums[i] >= path[-1]:
                    dfs(i + 1, path + [nums[i]]) # take nums[i] and start from i + 1
            
        dfs(0, [])
        return res


class Solution1(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/increasing-subsequences/discuss/97130/Java-20-lines-backtracking-solution-using-set-beats-100./101617
        # global dedup vs local dedup
        res = set()
        self.dfs(nums, 0, res, ())
        return res
    
    def dfs(self, nums, i, res, path):
        
        if len(path) >= 2:
            res.add(path[:])
        seen = set()

        for j in range(i, len(nums)):
            if nums[j] not in seen:
                seen.add(nums[j])
                if not path or path[-1] <= nums[j]:
                    self.dfs(nums, j + 1, res, path + (nums[j],))