class Solution:
    def numSquares(self, n: int) -> int:
        # interval DP
        # O(n**1.5) / O(n), 1 <= n <= 10**4
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1): # O(n)
            for j in range(1, int(math.sqrt(i)) + 1): # O(n**0.5)
                # make sure j^2 <= i
                dp[i] = min(dp[i], dp[i - j**2] + 1)
        return dp[-1]