class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # compress state to O(1)
        if len(prices) ==0:
            return 0
        profit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        # print(dp)
        return profit

        # O(n)/O(n)
        if len(prices) ==0:
            return 0
        dp = [0] * len(prices)
        minPrice = prices[0]
        for i in range(len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return dp[-1]