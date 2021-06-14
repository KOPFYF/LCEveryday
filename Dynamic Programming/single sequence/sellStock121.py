class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Template but slow, j = 2 & k = 1
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(0 - prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        return max(dp[-1])
            
        # compress state
        if len(prices) ==0:
            return 0
        profit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        # print(dp)
        return profit
    
        if len(prices) ==0:
            return 0
        dp = [0] * len(prices)
        minPrice = prices[0]
        for i in range(len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        # print(dp)
        return dp[-1]
    
        
        