class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # DP, coin change
        dp = [0] * (1 + target)
        for num in nums:
            if num <= target:
                dp[num] = 1
                
        for i in range(target + 1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i-num]
        return dp[-1]


# backtracking wit no memo, TLE
class Solution_TLE:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        n = len(nums)
        def dfs(target, path):
            if target < 0:
                return 
            if target == 0:
                res.append(path)
                return
            for num in nums:
                dfs(target - num, path + [num])
        dfs(target, [])
        return len(res)