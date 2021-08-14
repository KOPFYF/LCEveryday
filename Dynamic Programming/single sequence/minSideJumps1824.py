class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # DP bottom up 2D
        # dp[i][r] means the minimum jumps when the frog gets to point i lane r (0-index).
        # dp[i][r] = min([dp[i-1][r], dp[i-1][(r+1)%3] + 1, dp[i-1][(r+2)%3] + 1]) for r = 0, 1, 2
        n = len(obstacles) - 1
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][0] = dp[0][2] = 1
        dp[0][1] = 0
        
        for i in range(1, n):
            for j in range(3):
                if not (obstacles[i] == j + 1 or obstacles[i + 1] == j + 1):
                    dp[i][j] = min(dp[i-1][j], 
                                   dp[i-1][(j+1)%3] + 1, 
                                   dp[i-1][(j+2)%3] + 1)
        return min(dp[-1])