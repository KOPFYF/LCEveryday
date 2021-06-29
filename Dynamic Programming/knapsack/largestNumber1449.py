class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @functools.lru_cache(None)
        def dfs(i, target):  # return the maximum number built with the given target
            # we wont count overflow
            if i == len(cost) or target < 0:
                return float("-inf")

            if target == 0:  # reaching the target sum of cost
                return 0

            # 1 : take the current digit
            # 2 : the other one is not taking the current digit
            # as our i is moving from 0 to 8, the later coming digit should br greater than i,
            # so we are sure this can build the string optimally (in descending order)
            return max(dfs(i, target - cost[i]) * 10 + i + 1, dfs(i + 1, target))

        # retrieve the result by calling the function

        res = dfs(0, target)
        return str(res) if res > 0 else "0"
        
        @lru_cache(None)
        def dfs(i, target):
            if target == 0:
                return 0
            if i == len(cost) or target < 0: # overshoot
                return float('-inf')
            
            take = dfs(i + 1, target - cost[i]) * 10 + i + 1
            notake = dfs(i + 1, target)
            
            return max(take, notake)
        
        res = dfs(0, target)
        return str(res) if res > 0 else "0"


        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))
                