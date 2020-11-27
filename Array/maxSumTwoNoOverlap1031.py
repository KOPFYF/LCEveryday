class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        # Lsum, sum of the last L elements
        # Msum, sum of the last M elements
        # Lmax, max sum of contiguous L elements before the last M elements
        # Mmax, max sum of contiguous M elements before the last L elements
        
        for i in range(1, len(A)):
            A[i] += A[i - 1] # turn to prefix sum
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        # window  | --- L --- | --- M --- |(i)
        # pivot on i, left 
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M])

        # window  | --- M --- | --- L --- |(i)
        for i in range(L + M, len(A)):
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Mmax + A[i] - A[i - L])
        return res
    
#         # top-down DP, time out for the last 20 testcases 
#         # because this is a general template that could solve all (x, y, z) combinations
#         n = len(A)
#         print(sum(A))
#         memo = {}
#         def dfs(x, y, idx):
#             if idx >= n:
#                 return 0
#             if (x, y, idx) in memo:
#                 return memo[(x, y, idx)]
#             tmp0 = dfs(x, y, idx + 1) # dont take A[idx]
#             res, tmp1, tmp2 = -1, -1, -1
#             if x > 0 and idx + L - 1 < n:
#                 tmp1 = dfs(x - 1, y, idx + L) + sum(A[idx:idx + L])
#             if y > 0 and idx + M - 1 < n:
#                 tmp2 = dfs(x, y - 1, idx + M) + sum(A[idx:idx + M])
#             res = max(tmp0, tmp1, tmp2)
#             memo[(x, y, idx)] = res
#             print(memo)
#             return res
        
#         return dfs(1, 1, 0)