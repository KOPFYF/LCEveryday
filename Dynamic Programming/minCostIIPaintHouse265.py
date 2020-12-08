class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Bottom up
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0]
        
        for i in range(1, n):
            min1 = min(dp[i - 1])
            idx = dp[i - 1].index(min1)
            min2 = min(dp[i - 1][:idx] + dp[i - 1][idx + 1:])
            for j in range(k):
                if j == idx:
                    dp[i][j] = min2 + costs[i][j]
                else:
                    dp[i][j] = min1 + costs[i][j]
        
        return min(dp[n - 1])


class Solution2(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Bottom up, time O(nk) space O(1)
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in xrange(1, n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])
            for j in xrange(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])