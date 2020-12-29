class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atmost(A, K):
            count = collections.Counter()
            i, n = 0, len(A)
            res = 0
            for j in range(n):
                if count[A[j]] == 0: 
                    K -= 1
                count[A[j]] += 1
                while K < 0:
                    count[A[i]] -= 1
                    if count[A[i]] == 0: 
                        K += 1
                    i += 1
                res += j - i + 1
            return res
        return atmost(A, K) - atmost(A, K - 1)