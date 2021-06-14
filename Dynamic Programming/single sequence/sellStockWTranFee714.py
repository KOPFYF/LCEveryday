class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy, sell = -prices[0], 0
        for i in range(1, n):
            buy = max(sell - prices[i], buy)
            sell = max(buy + prices[i] - fee, sell)
        return max(sell, buy)
        
        # state 0: buy, could come from buy or sell last round
        # state 1: sell, last round must be hold so now you can sell
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = -prices[0], 0 # previously we cannot hold
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] - prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i] - fee, dp[i-1][1])
        # print(dp)
        return max(dp[-1])