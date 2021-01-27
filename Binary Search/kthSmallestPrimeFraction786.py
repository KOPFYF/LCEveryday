class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], k: int) -> List[int]:
        # Binary search m, 0 < m < 1, such that there are exact k pairs of (i, j) that A[i] / A[j] < m
        n = len(A)
        l, r = 0, 1.0
        while l < r:
            mid = (l + r) / 2
            max_f, cnt, j = 0.0, 0, 1
            for i in range(n - 1):
                # j = i # this line makes it 10 times slower
                while j < n and A[i] > mid * A[j]:
                    # i ... j ... find the smallest j such that A[i] / A[j] <= mid
                    j += 1
                cnt += (n - j)
                if n == j: break # to the end
                f = A[i] / A[j] # record the max float <= mid
                if f > max_f:
                    p, q, max_f = i, j, f
                    # print(p, q, max_f)
            if cnt == k:
                return [A[p], A[q]]
            elif cnt > k:
                r = mid
            else:
                l = mid
        return []


class Solution_lee215:
    def kthSmallestPrimeFraction(self, A, K):
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])