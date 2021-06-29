# https://leetcode.com/problems/k-inverse-pairs-array/discuss/1282496/Python-Short-O(nk)-solution-explained
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # dp[i][j] be number of permutation of numbers [1, ..., i], such that it has exactly j inverses.
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1]+ ... + dp[i-1][j-i+1]
        # because we can insert number i in i different places.
        # sp[i][j] = dp[i][0] + ... + dp[i][j]
        dp = [[1] * (k + 1) for _ in range(n + 1)]
        sp = [[1] * (k + 1) for _ in range(n + 1)]
        N = 10**9 + 7
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = sp[i-1][j] if j < i else (sp[i-1][j] - sp[i-1][j-i]) % N
                sp[i][j] = (sp[i][j-1] + dp[i][j]) % N
        
        return dp[-1][-1]