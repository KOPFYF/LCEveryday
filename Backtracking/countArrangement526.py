'''
Backtracking is O(n!)
dp O(n*2^n) 
'''

class Solution:
    def countArrangement(self, N: int) -> int:
        # backtracking -> dp
        res = 0
        nums = tuple(range(1, N+1))
        
        @lru_cache(None)
        def dfs(nums, i):
            if i == N+1: # to the end
                return 1
            res = 0
            for j, num in enumerate(nums): # try all the rest nums for index i
                if not num % i or not i % num:
                    res += dfs(tuple(nums[:j] + nums[j+1:]), i+1)
            return res
        
        return dfs(nums, 1)     