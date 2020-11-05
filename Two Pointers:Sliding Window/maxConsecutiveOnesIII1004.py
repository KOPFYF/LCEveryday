class Solution(object):
    def longestOnes(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # sliding window, time O(n) space O(1)
        i = 0
        for j in range(len(A)):
            k -= A[j] == 0
            if k < 0:
                k += A[i] == 0
                i += 1
        return j - i + 1