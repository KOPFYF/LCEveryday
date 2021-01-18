class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # iteration
        if len(nums) == 0:
            return [[]]
        res = []
        for i in set(nums): # set to dedup, 1,1,2 we only use one 1
            remaining = list(nums)
            remaining.remove(i) # remove current 
            for p in self.permuteUnique(remaining):
                res.append([i] + p)
        return res

# backtracking
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)