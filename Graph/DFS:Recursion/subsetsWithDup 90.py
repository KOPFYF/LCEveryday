class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(pos, path):
            res.append(path)
            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i - 1]: # skip dup
                    continue
                dfs(i + 1, path + [nums[i]])
                
        dfs(0, [])
        return res