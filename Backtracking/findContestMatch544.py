class Solution:
    def findContestMatch(self, n: int) -> str:
        a = list(map(str, range(1, n + 1)))
        # print([aa for aa in a])
        def dfs(A):
            n = len(A)
            if n == 1:
                return A[0]
            res = []
            for i in range(n // 2):
                res.append('(' + A[i] + ',' + A[n - 1 - i] + ')')
            # print(res)
            return dfs(res)
        return dfs(a)