class Solution(object):
    def shortestCommonSupersequence(self, A, B):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in xrange(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]

        # print(lcs(A, B))
        res, i, j = "", 0, 0
        for c in lcs(A, B):
            while A[i] != c:
                res += A[i]
                i += 1
            while B[j] != c:
                res += B[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + A[i:] + B[j:]


class Solution2:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # TLE on the last testcase
        m, n = len(str1), len(str2)
        @lru_cache(None)
        def dfs(i, j):
            if i == m or j == n:
                return str2[j:] or str1[i:]
            
            if str1[i] == str2[j]:
                res = str1[i] + dfs(i + 1, j + 1)
            else:
                tmp1 = str1[i] + dfs(i + 1, j)
                tmp2 = str2[j] + dfs(i, j + 1)
                res = tmp1 if len(tmp1) < len(tmp2) else tmp2
            return res
        return dfs(0, 0)