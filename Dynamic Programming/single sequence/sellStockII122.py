class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # state 0: buy, could come from buy or sell last round
        # state 1: sell, last round must be hold so now you can sell
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = -prices[0], 0 # previously we cannot hold
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] - prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        # print(dp)
        return max(dp[-1])
    
    
        # state 0: buy, could come from buy or sell last round
        # state 1: sell, last round must be hold so now you can sell
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0], dp[0][1] = float('-inf'), 0 # previously we cannot hold
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i-1][1] - prices[i-1], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i-1], dp[i-1][1])
        # print(dp)
        return max(dp[-1])
        
        
        # consider each pair of neighbors
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1)) 
        