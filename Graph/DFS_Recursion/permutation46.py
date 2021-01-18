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


# intuitive recursion
class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return [[]]
        res = []
        for i in range(n):
            for p in self.permute(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + p)
        return res


# backtracking, use position only, no slice 
class Solution3(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        def dfs(l):
            if l == n - 1:
                res.append(list(nums))
                return 
            for i in range(l, n):
                nums[l], nums[i] = nums[i], nums[l]   # swap nums[l] and nums[i]
                dfs(l + 1)
                nums[l], nums[i] = nums[i], nums[l]  # swap them back
        dfs(0)
        return res