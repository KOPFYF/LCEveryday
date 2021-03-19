class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        # O(n^3)
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y + 1] += matrix[x][y] # prefix sum row by row
        
        res = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                presum = defaultdict(int)
                presum[0] = 1
                s = 0
                for x in range(m):
                    s += matrix[x][y2] - (matrix[x][y1 - 1] if y1 > 0 else 0)
                    res += presum[s - target]
                    presum[s] += 1
        return res
        
        # O(n^4), TLE
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]
        
        res = 0
        for i in range(m):
            for j in range(n):
                for u in range(i + 1, m + 1):
                    for v in range(j + 1, n + 1):
                        sum_ = dp[u][v] - dp[i][v] - dp[u][j] + dp[i][j]
                        if sum_ == target:
                            res += 1
        return res