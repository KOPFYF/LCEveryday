class Solution(object):
    def permute(self, nums):
        # DFS
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            # search to the end and append current path
            res.append(path)
        for i in range(len(nums)):
            # fix nums[i] and find the permutation of the rest
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)