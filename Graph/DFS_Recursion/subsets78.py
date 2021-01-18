class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(path, pos):
            res.append(path)
            for i in range(pos, len(nums)):
                dfs(path + [nums[i]], i + 1)
        dfs([], 0)
        return res