class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Top down dp
        memo = {}
        def dfs(target):
            if target == 0: return 1
            if target in memo:
                return memo[target]
            res = 0
            for num in nums:
                if num <= target:
                    res += dfs(target - num)
            memo[target] = res
            return res
        
        return dfs(target)


class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # bottom up DP, coin change 2
        dp = [0] * (1 + target)
        for num in nums:
            if num <= target:
                dp[num] = 1
                
        for i in range(target + 1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i - num]
        return dp[-1]

        # or !!!
        dp = [0] * (1 + target)
        dp[0] = 1
        # for num in nums:
        #     if num <= target:
        #         dp[num] = 1
                
        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]


class Solution3_TLE:
    # backtracking
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