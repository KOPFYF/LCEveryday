class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = list(range(1, 10))
        def dfs(nums, k, n, path):
            if k < 0 or n < 0:
                return
            if k == 0 and n == 0:
                res.append(path)
            for i in range(len(nums)):
                # pruning!! dont look back because at most once
                # dfs(nums[:i] + nums[i+1:], k - 1, n - nums[i], path + [nums[i]])
                dfs(nums[i+1:], k - 1, n - nums[i], path + [nums[i]])
        dfs(nums, k, n, [])
        return res

# look back and use set, too slow!!
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        # seen = set()
        def dfs(target, path):
            if target < 0:
                return 
            if target == 0 and len(path) == k:
                res.add(tuple(sorted(path)))
                return
            for num in range(1, 10):
                if num not in path: # this cost O(n)
                    dfs(target - num, path + [num])
        dfs(n, [])
        return res