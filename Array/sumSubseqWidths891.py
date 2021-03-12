class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        For each number A[i]:

        There are i smaller numbers,
        so there are 2 ^ i sequences in which A[i] is maximum.
        we should do res += A[i] * 2^i

        There are n - i - 1 bigger numbers,
        so there are 2 ^ (n - i - 1) sequences in which A[i] is minimum.
        we should do res -= A[i] * 2^(n - i - 1)
        """
        # one pass O(nlogn)/O(1)
        res, n = 0, len(A)
        A.sort()
        for i in range(n):
            res += (1 << i) * A[i]
            res -= (1 << (n - i - 1)) * A[i]
        return res % (10**9 + 7)
        
        # presum postsum, O(nlogn)/O(n)
        res, n = 0, len(A)
        A.sort()
        presum, postsum = [A[0]] * n, [A[-1]] * n
        for i in range(1, n):
            presum[i] = presum[i - 1] + A[i]
            postsum[i] = postsum[i - 1] + A[n - 1 - i]
        
        for i in range(n):
            res += (1 << i) * (postsum[i] - presum[i])
        return res % (10**9 + 7)
        
        
        
        # bf, O(n^2), tle
        res, n = 0, len(A)
        A.sort()
        for i in range(n):
            for j in range(i+1, n):
                res += (1 << (j - i - 1)) * (A[j] - A[i])
        return res % (10**9 + 7)