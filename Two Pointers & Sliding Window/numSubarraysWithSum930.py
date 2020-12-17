class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # Sliding window
        i = cnt = res = 0
        for j in range(len(A)):
            cnt += A[j]
            while i < j and cnt > S:
                cnt -= A[i]
                i += 1
            if cnt < S: continue
            if cnt == S: res += 1
            k = i 
            # temp pointer deal with left zero
            while k < j and not A[k]:
                k += 1
                res += 1
        return res