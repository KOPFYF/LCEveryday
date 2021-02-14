class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(nums, target, pos, path):
            # [1a,1b,2,5,6,7,10], target 8
            if target == 0: 
                res.append(path)
                return 
            if target < 0 or pos == n: return
            
            dfs(nums, target - nums[pos], pos + 1, path + [nums[pos]]) # take current pos
            while pos <= n - 2 and nums[pos] == nums[pos + 1]:
                pos += 1
            dfs(nums, target, pos + 1, path) # no take
        
        dfs(candidates, target, 0, [])
        return res
        
         
        # soln 2
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