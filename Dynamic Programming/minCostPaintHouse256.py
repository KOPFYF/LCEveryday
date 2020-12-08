class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Top down
        if not costs: return 0
        n = len(costs)
        memo = {}
        def dfs(pos):
            if pos == 0:
                return costs[0]
            if pos in memo:
                return memo[pos]
            r, g, b = costs[pos]
            br, bg, bb = dfs(pos - 1)
            memo[pos] = min(bg, bb) + r, min(br, bb) + g, min(br, bg) + b
            return memo[pos]
        
        return min(dfs(n - 1))


class Solution2(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Bottom up
        n = len(costs)
        if n == 0: return 0
        
        dp = [[0] * 3 for _ in range(n)]
        dp[0] = costs[0]
        
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + costs[i][2]
        return min(dp[n-1])


class Solution3(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Bottom up 1d
        n = len(costs) 
        if n == 0: return 0
        
        dp = costs[0]
        
        for i in range(1, n):
            # Must use one line to update simutaniously!
            dp[0], dp[1], dp[2] = min(dp[1], dp[2]) + costs[i][0], \
                                  min(dp[0], dp[2]) + costs[i][1], \
                                  min(dp[1], dp[0]) + costs[i][2]
        return min(dp)