class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, pos, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(pos, len(nums)):
            # here index is i because we can use unlimited times
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


class Solution1:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums, pos, target, path):
            if target < 0:
                return 
            if target == 0:
                res.append(path[:])
                return
                
            for i in range(pos, len(nums)):
                path.append(nums[i])
                dfs(nums, i, target - nums[i], path)
                path.pop()
        
        dfs(nums, 0, target, [])
        return res


class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, pos, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]:
                # [1a,1b,2,5,6,7,10], target 8, [1,2,5] will repeat if not dedup
                continue
            if nums[i] > target:
                break
            # We change the start to `i + 1` to remove avoid dup
            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)