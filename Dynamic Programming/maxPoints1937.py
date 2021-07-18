'''
https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344888/C%2B%2B-dp-from-O(m-*-n-*-n)-to-O(m-*-n)

To further reduce the time complexity, I found that there is some similar calculation when we are trying to find the max. That is dp[i - 1][k] - k (or + k depends on the position). To reduce to the smaller problem, we assume that all the max value is from the left side of the current position. With this assumption, the abs(k - j) can be changed to j - k. Due to other values (e.g. points[i][j]) are fixed. The problem becomes to find the max dp[i - 1][k] + k in the left. That is

dp[i][j] = max(dp[i - 1][k] + k) + points[i][j] - j for all 0 <= k <= j
You may notice that some of the sign is reversed, that is because of we need to subtract the cost.

Now, the right side is similar. If we assume max value is from the right side. The relation will be:

dp[i][j] = max(dp[i - 1][k] - k) + points[i][j] + j for all j <= k <= points[i].size() - 1
The actual answer will be either from the left side or right side.

'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
            
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
            
        for i in range(1, m):
            dp_left, dp_right = [0] * n, [0] * n
            dp_left[0] = dp[i - 1][0] + 0
            for k in range(1, n):
                dp_left[k] = max(dp_left[k - 1], dp[i - 1][k] + k)
            
            dp_right[-1] = dp[i - 1][-1] - (n - 1)
            for k in range(n - 2, -1, -1):
                dp_right[k] = max(dp_right[k + 1], dp[i - 1][k] - k)
            
            
            for j in range(n):
                dp[i][j] = max(dp_left[j] - j, dp_right[j] + j) + points[i][j]
        
        # print(dp[-1])
        return max(dp[-1])
    
    
        
        # TLE
        # 1 <= m, n <= 10**5, 
        # 1 <= m * n <= 10**5, O(mn), O(mn^2)
        m, n = len(points), len(points[0])
            
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
            
        for i in range(1, m):
            for j in range(n):
                # dp[i][j] = dp[i - 1][j]
                for jj in range(n):
                    dp[i][j] = max(points[i][j] + dp[i-1][jj] - abs(j - jj), dp[i][j])
        
        # print(dp[-1])
        return max(dp[-1])
                
            
        
        
        